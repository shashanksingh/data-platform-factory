from abc import abstractmethod
from typing import Dict
import abc

from pydantic import BaseModel, ConfigDict

EXTRACT_TYPE: Dict = {}


class Extract(BaseModel, abc.ABC):
    model_config = ConfigDict(extra="forbid")
    source: str

    @property
    @abc.abstractmethod
    def template(self):
        """ The template for the extract"""

    def __str__(self):
        return self.source
