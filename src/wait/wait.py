from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class Wait(BaseModel):
    model_config = ConfigDict(extra="forbid")
    after_source: Optional[str] = None
    before_transform: Optional[str] = None
    before_load: Optional[str] = None
    before_report: Optional[str] = None
