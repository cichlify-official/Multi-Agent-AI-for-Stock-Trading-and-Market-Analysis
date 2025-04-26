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
