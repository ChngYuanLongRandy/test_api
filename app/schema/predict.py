from typing import List, Optional, Any
from pydantic import BaseModel
from src.preprocessing.validation import multiple_inputSchema


class PredictionResults(BaseModel):
    Prediction: List[Any] | None = None
    Errors: Any | None = None
    Version: str


class Multiple_multipleinputs(BaseModel):
    inputs: List[multiple_inputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [{
                    "ID": "TIG1GE",
                    "Gender": "Male",
                    "Smoke": "yes",
                    "Diabetes": "Normal",
                    "Age": 50,
                    "Ejection Fraction": "low",
                    "Sodium": 141,
                    "Creatinine": 0.7,
                    "Pletelets": 266000,
                    "Creatinine phosphokinase": 185,
                    "Blood Pressure": 105,
                    "Hemoglobin": 12.3,
                    "Height": 180,
                    "Weight": 93,
                    "Favorite color": "Green"
                }]
            }


        }
