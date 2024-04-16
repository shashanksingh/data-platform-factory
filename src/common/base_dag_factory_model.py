from abc import abstractmethod

from pydantic import BaseModel


class BaseDAGFactoryModel(BaseModel):
    type: str

    @property
    @abstractmethod
    def template(self):
        """The template"""
