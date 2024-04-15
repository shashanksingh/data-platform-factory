from pydantic import ConfigDict

from src.common.base_dag_factory_model import BaseDAGFactoryModel


class Extract(BaseDAGFactoryModel):
    model_config = ConfigDict(extra="forbid")
    conn_id: str

    def __str__(self):
        return self.conn_id
