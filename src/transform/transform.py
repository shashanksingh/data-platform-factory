from typing import Optional

from pydantic import BaseModel, Field


class Transform(BaseModel):
    source: Optional[str] = None
