from pydantic import BaseModel


class HealthSchema(BaseModel):
    apiVersion: str
    modelVersion: str
    modelName: str
