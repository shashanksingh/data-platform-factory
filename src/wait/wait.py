from typing import Optional

from pydantic import BaseModel, Field


class Wait(BaseModel):
    after_source: Optional[str] = None
    before_transform: Optional[str] = None
    before_load: Optional[str] = None
    before_report: Optional[str] = None
