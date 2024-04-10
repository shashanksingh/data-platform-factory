from pydantic import BaseModel, ConfigDict


class Extract(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source: str
