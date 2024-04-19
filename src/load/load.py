from pydantic import BaseModel, ConfigDict, computed_field


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")
    conn_id: str

    def __str__(self):
        return self.conn_id

    @computed_field(return_type=str)
    def template(self):
        return f"load/{self.__class__.__name__}.py.jinja"
