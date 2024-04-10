from pydantic import BaseModel, ConfigDict


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")

    destination: str
