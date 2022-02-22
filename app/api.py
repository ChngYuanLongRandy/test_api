import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from app.config.settings import API_VERSION, APP_NAME
from src.model.predict import make_prediction_inputs_api, make_prediction_inputs_api_dict
from app.schema import health, predict
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


@app.post('/predict')#, response_model=predict.PredictionResults, status_code=200)
async def predict_value(input_data: predict.multipleinputs):
    logger.info("predict function accessed")
    logger.info(f"input_data values: {input_data.inputs}")

    logger.info(f"input data with jsonable encoder: {jsonable_encoder(input_data.inputs)}")

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"input_df with pd DataFrame: {input_df}")
    logger.info(f"Cols: {input_df.columns}")
    logger.info(f"1st row: {input_df.iloc[0,:]}")

    #results = make_prediction_inputs_api_dict(input_data=input_df)
    results = make_prediction_inputs_api(input_data=input_df, proba=True)

    logger.info(f"results: {results}")

    if results['Errors'] is not None:
        raise HTTPException(status_code=400, detail=json.loads(results["Errors"]))

    logger.info(f"Prediction results: {results.get('Prediction')}")
    logger.info(f"results type : {type(results)}")
    logger.info(f"results items : {results.items()}")

    result_prediction = results.get('Prediction')
    result_error = results.get('Errors')
    result_version = results.get('Version')

    logger.info(f"result_prediction: {type(result_prediction)}")
    logger.info(f"result_error : {result_error}")
    logger.info(f"result_version : {result_version}")

    return results

@app.post('/predictv2')#, response_model=predict.PredictionResults, status_code=200)
def predict_valuev2(input_data: predict.multipleinputs):

    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    return input_df