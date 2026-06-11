# indie:lang_version = 5
# ============================================================================
#  BTC Scalping Pro v2  (Indie v5 - function form, Exness-safe)
#  Bollinger-Band mean reversion + RSI + trend filter (EMA200), with an
#  optional MACD filter (Strict mode). Each signal shows a Stop (SL) and a
#  Target (TP = middle band).
#  Chart = 5m. Not financial advice. Use the smallest lot + a stop-loss.
#
#  Strict mode ON  = require MACD agreement  -> fewer, higher-quality signals
#  Strict mode OFF = ignore MACD             -> more signals
# ============================================================================
from math import nan
from indie import indicator, param, plot, color
from indie.algorithms import Ema, Rsi, Macd, Atr, Bb


@indicator('BTC Scalping Pro', overlay_main_pane=True)
@param.bool('strict', default=True, title='Strict mode (require MACD)')
@param.int('bb_length', default=20, min=2, title='BB length')
@param.float('bb_mult', default=2.0, min=0.1, title='BB deviation')
@param.int('rsi_length', default=14, min=2, title='RSI length')
@param.float('rsi_os', default=40.0, title='RSI oversold (BUY below)')
@param.float('rsi_ob', default=60.0, title='RSI overbought (SELL above)')
@param.int('macd_fast', default=12, min=1, title='MACD fast')
@param.int('macd_slow', default=26, min=1, title='MACD slow')
@param.int('macd_signal', default=9, min=1, title='MACD signal')
@param.int('trend_length', default=200, min=2, title='Trend EMA (bigger trend)')
@param.int('atr_length', default=14, min=1, title='ATR length')
@param.float('atr_mult', default=1.5, min=0.1, title='ATR stop multiplier')
@plot.line('bb_upper', title='BB upper', color=color.BLUE)
@plot.line('bb_basis', title='BB basis', color=color.ORANGE)
@plot.line('bb_lower', title='BB lower', color=color.BLUE)
@plot.line('trend', title='Trend EMA', color=color.GREEN)
@plot.marker(style=plot.marker_style.LABEL, position=plot.marker_position.BELOW, color=color.GREEN, text='BUY', size=4, title='BUY')
@plot.marker(style=plot.marker_style.LABEL, position=plot.marker_position.ABOVE, color=color.RED, text='SELL', size=4, title='SELL')
@plot.marker(style=plot.marker_style.CROSS, position=plot.marker_position.CENTER, color=color.RED, text='SL', size=3, title='Stop')
@plot.marker(style=plot.marker_style.CROSS, position=plot.marker_position.CENTER, color=color.BLUE, text='TP', size=3, title='Target')
def Main(self, strict, bb_length, bb_mult, rsi_length, rsi_os, rsi_ob,
         macd_fast, macd_slow, macd_signal, trend_length, atr_length, atr_mult):

    lower, middle, upper = Bb.new(self.close, bb_length, bb_mult)
    rsi = Rsi.new(self.close, rsi_length)
    macd_line, macd_sig, macd_hist = Macd.new(self.close, macd_fast, macd_slow, macd_signal)
    ema_trend = Ema.new(self.close, trend_length)
    atr = Atr.new(atr_length)

    # Bigger-trend filter
    trend_up = self.close[0] > ema_trend[0]
    trend_dn = self.close[0] < ema_trend[0]

    # MACD filter only applies in Strict mode
    macd_ok_buy = macd_line[0] > macd_sig[0] if strict else True
    macd_ok_sell = macd_line[0] < macd_sig[0] if strict else True

    # LONG: bounce back up off the lower band, oversold, (MACD up), uptrend
    long_cond = (self.close[0] > lower[0] and self.close[1] <= lower[1]
                 and rsi[0] < rsi_os and macd_ok_buy and trend_up)
    # SHORT: drop back down off the upper band, overbought, (MACD down), downtrend
    short_cond = (self.close[0] < upper[0] and self.close[1] >= upper[1]
                  and rsi[0] > rsi_ob and macd_ok_sell and trend_dn)

    buy_val = self.low[0] if long_cond else nan
    sell_val = self.high[0] if short_cond else nan

    # Stop (ATR) and Target (middle band) shown only on signal bars
    stop_val = nan
    target_val = nan
    if long_cond:
        stop_val = self.low[0] - atr_mult * atr[0]
        target_val = middle[0]
    if short_cond:
        stop_val = self.high[0] + atr_mult * atr[0]
        target_val = middle[0]

    # 8 returns <-> 8 @plot decorators (same order)
    return upper[0], middle[0], lower[0], ema_trend[0], buy_val, sell_val, stop_val, target_val
