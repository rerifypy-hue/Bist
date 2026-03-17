from fastapi import FastAPI
from analysis import get_signal

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/signal/{ticker}")
def signal(ticker: str):
    result = get_signal(ticker)
    return {"ticker": ticker, "signal": result}
