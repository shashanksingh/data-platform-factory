from typing import Optional
from pydantic import BaseModel, ConfigDict
from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait
from src.dag.dag import DAG


class DAGDescription(BaseModel):
    model_config = ConfigDict(extra="forbid")

    dag: DAG
    extract: Extract
    transforms: Optional[Transform] = None
    load: Load
    report: Optional[Report] = None
    wait: Optional[Wait] = None
