# MTF Confluence Signal — BTC + Gold

A multi-timeframe BUY/SELL signal indicator for the **Exness Web Trading** code editor
(the editor that says *"Powered by Indie"* at the bottom). It only flags a trade when
**trend + momentum + market session all agree** — your "combine all three" setup.

File: [`mtf_confluence_signal.py`](mtf_confluence_signal.py)

---

## ⚠️ Read this first (important)

- **This is NOT financial advice and NOT a guarantee.** No indicator is ever 100% accurate.
  It helps your *timing and discipline* — it does not predict the future.
- Your account in the screenshot is a **Real (real-money)** account. **Test on a DEMO account first.**
- **Always use a stop-loss.** The indicator draws a suggested ATR stop level to help.
- It **cannot** connect to OKX, GitHub, or any website for live data. Indie code runs in a
  sandbox and can only see the chart's own candles. (GitHub is only used here to *store* the code.)

---

## How the signal works

| Timeframe | Job | Logic |
|-----------|-----|-------|
| **4h** | Trend direction (the boss) | EMA 20 vs EMA 50 → up or down |
| **1.5h (90m)** | Trend confirmation | MACD histogram agrees with the 4h trend |
| **15m** | Momentum health | RSI not overbought (buys) / not oversold (sells) |
| **5m** | Entry trigger | A fresh 5m EMA cross = the "go" moment |
| **Session** | Time filter | Only during London / New York / Tokyo hours (optional) |

A **BUY** appears only when: session OK **and** 4h up **and** 90m up **and** 15m RSI healthy **and** a 5m bullish cross.
**SELL** is the mirror image. Because every condition must line up, signals are **rare by design** —
you may go hours with none. That is intended (you chose the safest mode).

---

## Install (step by step)

1. In Exness Web Trading, open the chart and set the timeframe to **5m** (top-left, where it shows `5m`).
2. Click the **`{}`** code icon on the left toolbar to open the Indie editor.
3. **Delete** the sample code in the editor.
4. Open [`mtf_confluence_signal.py`](mtf_confluence_signal.py), copy **everything**, and paste it in.
5. Click **Save**, then **Add to chart**.
6. Open the indicator **settings (⚙ / pencil)** and set it up for your market (below).

### Settings for each market
- **Gold (XAU/USD):** leave **"Use market sessions" = ON**.
- **BTC (24/7):** turn **"Use market sessions" = OFF**.
- If the **90m** confirmation shows nothing or errors: set **"Confirm timeframe" = 1h**.

---

## Tuning tips
- **Too few signals?** Turn sessions OFF, or widen the RSI blocks (e.g. buy-max 75, sell-min 25),
  or use a faster confirm timeframe (15m).
- **Too many / messy signals?** Keep sessions ON, tighten RSI (buy-max 60, sell-min 40),
  or raise the EMA lengths.
- **Wider/tighter stop:** change the **ATR multiplier** (1.5 = normal, 2.0 = wider, 1.0 = tighter).

---

## If you see an error in the editor
- **Anything about a timeframe being lower than the chart** → your chart is not on 5m. Set it to 5m.
- **The 90m line is blank / errors** → change "Confirm timeframe" to `1h` in settings.
- **An error pointing at the `self.time` / session line** → tell me; some builds report time in
  milliseconds instead of seconds and the one number on that line needs adjusting.

---

## ملخص بالعربية (Arabic summary)

- هذا المؤشر يعمل داخل محرر **Exness Web Trading** ("Powered by Indie").
- **يجب وضع الشارت على فريم 5 دقائق** — هذا إلزامي حتى يستطيع قراءة فريمات 15م و90م و4 ساعات.
- يظهر سهم **شراء/بيع** فقط عندما يتفق: اتجاه 4 ساعات + تأكيد 90 دقيقة + زخم 15 دقيقة + جلسة السوق + إشارة دخول على 5 دقائق.
- **للذهب:** فعّل "Use market sessions". **للبيتكوين:** أوقفه.
- إذا لم يظهر فريم 90 دقيقة، غيّره إلى 1h من الإعدادات.
- ⚠️ ليست نصيحة مالية ولا ضمان. **جرّب على حساب تجريبي أولاً، واستخدم دائماً وقف الخسارة.**
