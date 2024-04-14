from typing import Dict

from pydantic import BaseModel, ConfigDict

EXTRACT_TYPE: Dict = {}


class Extract(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str

    def __str__(self):
        return self.source
