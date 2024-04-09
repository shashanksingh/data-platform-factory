from pydantic import BaseModel, Field


class Load(BaseModel):
    destination: str
