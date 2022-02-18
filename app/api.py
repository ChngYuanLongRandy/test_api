import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from config.settings import API_VERSION, APP_NAME
from src.model.predict import make_prediction_inputs_api
from schema import health, predict
import json
from loguru import logger

logger.info("api.py file accessed")

# I initialise these as static first
MODEL_NAME = 'Random Forest'
MODEL_VERSION = '0.0.8'

app = FastAPI()


# root, display a rudimentary homepage
@app.get('/')
def homepage():
    logger.info("homepage function accessed")
    return {'message': f'Welcome to {APP_NAME}'}


@app.get("/health", response_model=health.HealthSchema, status_code=200)
def health_of_api() -> dict:
    logger.info("health_of_api function accessed")
    logger.info(f"Parameters are apiVersion: {API_VERSION},modelVersion: {MODEL_VERSION},modelName: {MODEL_NAME}")
    _health = health.HealthSchema(apiVersion=API_VERSION,
                                  modelVersion=MODEL_VERSION,
                                  modelName=MODEL_NAME)

    return _health.dict()


@app.post('/predict', response_model=predict.PredictionResults, status_code=200)
async def predict_value(input_data: predict.Multiple_multipleinputs):
    logger.info("health_of_api function accessed")
    logger.info(f"input_data values: {input_data.inputs}")

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    results = make_prediction_inputs_api(input_data=input_df)

    if results['errors'] is not None:
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")

    return results
