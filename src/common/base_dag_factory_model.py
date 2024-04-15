from pydantic import BaseModel


class BaseDAGFactoryModel(BaseModel):
    type: str
