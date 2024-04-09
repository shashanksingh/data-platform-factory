from typing import Optional
from pydantic import BaseModel, Field
from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGDescription(BaseModel):
    extract: Extract
    transforms: Optional[Transform] = None
    load: Load
    report: Optional[Report] = None
    wait: Wait
