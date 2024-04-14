from pydantic import BaseModel, ConfigDict


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")

    destination: str

    def __str__(self):
        return self.destination
