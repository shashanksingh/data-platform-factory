from pydantic import BaseModel, Field, ConfigDict


class Extract(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source: str
