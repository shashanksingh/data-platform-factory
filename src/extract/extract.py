from typing import Dict

from pydantic import BaseModel, ConfigDict

EXTRACT_TYPE: Dict = {}


class Extract(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
