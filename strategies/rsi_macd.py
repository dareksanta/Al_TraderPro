import pandas as pd

def generate_signal(df):
    # Wylicz MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=9, adjust=False).mean()

    # Wylicz RSI
    delta = df['Close'].diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ema_up = up.ewm(com=13, adjust=False).mean()
    ema_down = down.ewm(com=13, adjust=False).mean()
    rs = ema_up / ema_down
    rsi = 100 - (100 / (1 + rs))

    # Reguła generowania sygnału
    if macd.iloc[-1] > signal_line.iloc[-1] and rsi.iloc[-1] < 70:
        return "BUY"
    elif macd.iloc[-1] < signal_line.iloc[-1] and rsi.iloc[-1] > 30:
        return "SELL"
    else:
        return "WAIT"
