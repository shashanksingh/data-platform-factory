from pydantic import BaseModel, ConfigDict


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")
    conn_id: str

    def __str__(self):
        return self.conn_id
