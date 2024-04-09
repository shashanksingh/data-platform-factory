from pydantic import BaseModel, Field


class Wait(BaseModel):
    after_source: str
    before_transform: str
    before_load: str
    before_report: str
