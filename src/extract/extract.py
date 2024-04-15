from abc import abstractmethod, ABC
from typing import Dict

from pydantic import BaseModel, ConfigDict

EXTRACT_TYPE: Dict = {}


class Extract(BaseModel, ABC):
    model_config = ConfigDict(extra="forbid")
    name: str
    conn_id: str
    type: str  # is used to define handler

    __handler: Dict = {}

    @classmethod
    def register_handler(cls, handler_name:str, handler_class: "Extract") -> None:
        cls.__handler[handler_name] = handler_class

    @classmethod
    def get_handler(cls, handler_name: str) -> str:
        return cls.__handler.get(handler_name, "")

    @property
    @abstractmethod
    def template(self):
        """The template for the extract"""

    def __str__(self):
        return self.name
