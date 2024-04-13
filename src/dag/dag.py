from typing import Optional, List
from pydantic import BaseModel, ConfigDict, field_validator

AIRFLOW_VALID_SCHEDULE_STRINGS = {"@continuous"}


class DAG(BaseModel):
    model_config = ConfigDict(extra="forbid")

    start_date: Optional[str] = None
    catchup: Optional[bool] = False
    tags: Optional[List[str]] = ["example"]
    schedule: Optional[str] = "@daily"

    @field_validator("schedule")
    @classmethod
    def schedule_must_be_from_valid_airflow_list(cls, value: str) -> str:
        if value not in AIRFLOW_VALID_SCHEDULE_STRINGS:
            raise ValueError("must contain a space")
        return value.title()
