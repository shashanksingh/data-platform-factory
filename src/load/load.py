from pydantic import BaseModel, Field, ConfigDict


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")

    destination: str
