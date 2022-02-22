from typing import List, Optional, Any
from pydantic import BaseModel
from src.preprocessing.validation import inputSchema


class PredictionResults(BaseModel):
    Errors: Optional[Any]
    version: str
    Prediction: Optional[List[float]] | None

class test_inputs(BaseModel):
    input1 : str
    input2 : str
    input3 : str

class multipleinputs(BaseModel):
    inputs: List[inputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [{
                    #"ID": "TIG1GE",
                    "Gender": "Male",
                    "Smoke": "Yes",
                    "Diabetes": "Normal",
                    "Age": 50,
                    "Ejection_Fraction": "Low",
                    "Sodium": 141,
                    "Creatinine": 0.7,
                    "Pletelets": 266000,
                    "CK": 185,
                    "BP": 105,
                    "Hemoglobin": 12.3,
                    "Height": 180,
                    "Weight": 93
                    #"BMI": 32
                }]
            }
        }
