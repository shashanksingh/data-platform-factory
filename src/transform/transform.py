from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class Transform(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: Optional[str] = None
