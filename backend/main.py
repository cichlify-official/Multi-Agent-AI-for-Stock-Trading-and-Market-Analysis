from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "It works!"}

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


class PredictRequest(BaseModel):
    features: list  # input features for prediction

@app.post("/predict")
async def predict(request: PredictRequest):
    # TODO: Load your model here and do real prediction
    fake_prediction = sum(request.features)  # just a fake example
    return {"prediction": fake_prediction}
