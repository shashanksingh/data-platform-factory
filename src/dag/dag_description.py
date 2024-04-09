from typing import List

from pydantic import BaseModel, Field

from ..extract.extract import Extract
from ..load.load import Load
from ..report.report import Report
from ..transform.transform import Transform
from ..wait.wait import Wait


class DAGDescription(BaseModel):
    extract: Extract
    transforms: List[Transform]
    load: Load
    report: List[Report]
    wait: Wait
