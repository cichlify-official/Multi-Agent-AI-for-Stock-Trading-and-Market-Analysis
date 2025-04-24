from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from .trading_bot import run_bot
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict")
def predict(ticker: str = Query(..., description="Stock ticker symbol")):
    try:
        result = run_bot(ticker)
        if isinstance(result, pd.DataFrame):
            return result.to_dict(orient="records")
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

from fastapi import FastAPI
from backend.trading_bot import run_bot

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent AI Trading API up and running 🚀"}

@app.post("/start-bot")
def start_bot():
    run_bot()
    return {"status": "Bot started"}

@app.post("/stop-bot")
def stop_bot():
    # You’ll implement stop logic in your agent
    return {"status": "Bot stopped"}

@app.get("/data")
def get_data():
    # Return live/recorded results from trading
    return {"price": 123.45, "agent": "Alpha", "action": "Buy"}
