import yfinance as yf
import pandas as pd

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def get_signal(ticker):
    df = yf.download(f"{ticker}.IS", period="3mo")

    df["MA20"] = df["Close"].rolling(20).mean()
    df["MA50"] = df["Close"].rolling(50).mean()
    df["RSI"] = compute_rsi(df["Close"])

    last = df.iloc[-1]

    score = 0

    if last["MA20"] > last["MA50"]:
        score += 1
    if last["RSI"] < 30:
        score += 1
    if last["RSI"] > 70:
        score -= 1

    if score >= 2:
        return "STRONG BUY"
    elif score == 1:
        return "BUY"
    elif score == 0:
        return "HOLD"
    else:
        return "SELL"
