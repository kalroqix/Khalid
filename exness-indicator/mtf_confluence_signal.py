# indie:lang_version = 5
# =============================================================================
#  MTF Confluence Signal — BTC   (function form; works in the Exness editor)
#
#  Put the chart on the 5-MINUTE timeframe. Sessions are OFF by default (BTC 24/7).
#
#  NOTE: true higher-timeframe candle access (real 4h/90m/15m) needs the "class"
#  form, which errors on this Exness build ("0 outputs"). So the higher
#  timeframes are APPROXIMATED with longer indicator lengths on the 5m chart:
#     Trend    ~ EMA 50 vs EMA 200        (slow trend direction)
#     Confirm  ~ slow MACD 24/52/18       (histogram sign)
#     Momentum ~ RSI 14                    (above/below 50)
#     Entry    = native 5m EMA 9/21 cross  (the actual trigger)
#  A BUY/SELL only fires when all of them agree. Not financial advice.
# =============================================================================
from math import nan
from indie import indicator, param, plot, color
from indie.algorithms import Ema, Rsi, Macd, Atr
from indie.math import cross_over, cross_under


@indicator('MTF Confluence Signal (BTC)', overlay_main_pane=True)
@param.int('ema_fast', default=9, min=1, title='5m entry EMA fast')
@param.int('ema_slow', default=21, min=1, title='5m entry EMA slow')
@param.int('trend_fast', default=50, min=1, title='Trend EMA fast')
@param.int('trend_slow', default=200, min=1, title='Trend EMA slow')
@param.int('macd_fast', default=24, min=1, title='Confirm MACD fast')
@param.int('macd_slow', default=52, min=1, title='Confirm MACD slow')
@param.int('macd_sig', default=18, min=1, title='Confirm MACD signal')
@param.int('rsi_len', default=14, min=1, title='RSI length')
@param.float('rsi_buy_min', default=50.0, title='RSI min for BUY')
@param.float('rsi_sell_max', default=50.0, title='RSI max for SELL')
@param.bool('use_session', default=False, title='Use session gate (OFF for BTC 24/7)')
@param.int('sess_start', default=7, min=0, max=23, title='Session start hour (UTC)')
@param.int('sess_end', default=20, min=0, max=23, title='Session end hour (UTC)')
@param.bool('show_stop', default=True, title='Show ATR stop marker')
@param.int('atr_len', default=14, min=1, title='ATR length')
@param.float('atr_mult', default=1.5, min=0.1, title='ATR stop multiplier')
@plot.line('trend', title='Trend EMA slow', color=color.BLUE)
@plot.marker(style=plot.marker_style.LABEL, position=plot.marker_position.BELOW, color=color.GREEN, text='BUY', size=4, title='BUY')
@plot.marker(style=plot.marker_style.LABEL, position=plot.marker_position.ABOVE, color=color.RED, text='SELL', size=4, title='SELL')
@plot.marker(style=plot.marker_style.CROSS, position=plot.marker_position.CENTER, color=color.ORANGE, size=3, title='Stop')
def Main(self, ema_fast, ema_slow, trend_fast, trend_slow,
         macd_fast, macd_slow, macd_sig, rsi_len, rsi_buy_min, rsi_sell_max,
         use_session, sess_start, sess_end, show_stop, atr_len, atr_mult):

    # Trend (higher-timeframe proxy): EMA fast vs slow
    t_fast = Ema.new(self.close, trend_fast)
    t_slow = Ema.new(self.close, trend_slow)
    trend_up = t_fast[0] > t_slow[0]
    trend_dn = t_fast[0] < t_slow[0]

    # Confirm: slow MACD histogram sign (Macd returns: line, signal, histogram)
    macd_line, macd_signal, macd_hist = Macd.new(self.close, macd_fast, macd_slow, macd_sig)
    confirm_up = macd_hist[0] > 0.0
    confirm_dn = macd_hist[0] < 0.0

    # Momentum: RSI vs 50
    rsi = Rsi.new(self.close, rsi_len)
    rsi_ok_buy = rsi[0] >= rsi_buy_min
    rsi_ok_sell = rsi[0] <= rsi_sell_max

    # Entry trigger: native 5m EMA cross
    e_fast = Ema.new(self.close, ema_fast)
    e_slow = Ema.new(self.close, ema_slow)
    cross_up = cross_over(e_fast, e_slow)
    cross_dn = cross_under(e_fast, e_slow)

    # Session gate (default OFF). No chained comparisons allowed.
    session_ok = True
    if use_session:
        utc_hour = (self.time[0] % 86400.0) / 3600.0
        in_session = False
        if sess_start <= sess_end:
            if (utc_hour >= sess_start) and (utc_hour < sess_end):
                in_session = True
        else:
            if (utc_hour >= sess_start) or (utc_hour < sess_end):
                in_session = True
        session_ok = in_session

    # Combine ALL conditions
    buy_signal = cross_up and trend_up and confirm_up and rsi_ok_buy and session_ok
    sell_signal = cross_dn and trend_dn and confirm_dn and rsi_ok_sell and session_ok

    # Markers: return a plain price, or nan to hide on that bar
    buy_marker = self.low[0] if buy_signal else nan
    sell_marker = self.high[0] if sell_signal else nan

    atr = Atr.new(atr_len)
    stop_marker = nan
    if show_stop:
        if buy_signal:
            stop_marker = self.low[0] - atr_mult * atr[0]
        if sell_signal:
            stop_marker = self.high[0] + atr_mult * atr[0]

    # 4 returned values <-> 4 @plot decorators, in the same order
    return t_slow[0], buy_marker, sell_marker, stop_marker
