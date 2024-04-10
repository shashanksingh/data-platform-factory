from typing import Optional
from pydantic import BaseModel, Field


class Transform(BaseModel):
    name: Optional[str] = None
