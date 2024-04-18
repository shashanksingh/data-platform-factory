from pydantic import ConfigDict, computed_field

from src.common.base_dag_factory_model import BaseDAGFactoryModel


class Extract(BaseDAGFactoryModel):
    model_config = ConfigDict(extra="forbid")
    conn_id: str

    @computed_field(return_type=str)
    def template(self):
        return f"extract/{self.__class__.__name__}.py.jinja"

    def __str__(self):
        return self.conn_id
