from pydantic import BaseModel, Field


class Extract(BaseModel):
    source: str
