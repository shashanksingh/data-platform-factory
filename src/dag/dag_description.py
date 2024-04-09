from typing import List

from pydantic import BaseModel, Field

from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGDescription(BaseModel):
    extract: Extract
    transforms: List[Transform]
    load: Load
    report: List[Report]
    wait: Wait
