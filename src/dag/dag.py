from typing import Optional, List
from pydantic import BaseModel, ConfigDict, field_validator

AIRFLOW_VALID_SCHEDULE_STRINGS = {
    "@continuous",
    "@daily",
    "@weekly",
    "@once",
    "@hourly",
    "@monthly",
}

DAG_TYPE_MUST_BE_VALID = {"postgresql-to-postgresql"}


class DAG(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    start_date: Optional[str] = None
    catchup: Optional[bool] = False
    tags: Optional[List[str]] = ["example"]
    schedule: Optional[str] = "@daily"

    @field_validator("schedule")
    @classmethod
    def schedule_must_be_from_valid_airflow_list(cls, value: str) -> str:
        if value not in AIRFLOW_VALID_SCHEDULE_STRINGS:
            raise ValueError(
                f"must be from AIRFLOW_VALID_SCHEDULE_STRINGS {AIRFLOW_VALID_SCHEDULE_STRINGS}"
            )
        return value

    @field_validator("type")
    @classmethod
    def type_must_be_from_valid_airflow_list(cls, value: str) -> str:
        if value not in DAG_TYPE_MUST_BE_VALID:
            raise ValueError(
                f"must be from DAG_TYPE_MUST_BE_VALID {DAG_TYPE_MUST_BE_VALID}"
            )
        return value
