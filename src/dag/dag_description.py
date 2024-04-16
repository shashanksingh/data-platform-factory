from __future__ import annotations

from typing import Optional, Dict
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

    def convert_to_dict(self) -> Dict:
        """
        TODO
        model_dump should have recursively done this, but it didnt so this is bit of hack
        description :
        :return: Dict representation of models
        """
        return {
            "dag": self.model_dump().get("dag"),
            "extract": self.extract.model_dump(),
            "transforms": self.transforms.model_dump() if self.transforms else None,
            "load": self.load.model_dump(),
            "report": self.report.model_dump() if self.report else None,
            "wait": self.wait.model_dump() if self.wait else None,
            "toml": self.model_dump(),
        }
