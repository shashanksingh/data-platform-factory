from pydantic import BaseModel, Field


class Transform(BaseModel):
    source: str
