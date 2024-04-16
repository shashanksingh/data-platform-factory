from abc import abstractmethod

from pydantic import BaseModel


class BaseDAGFactoryModel(BaseModel):
    type: str

    @property
    @abstractmethod
    def template(self):
        """The template"""

    def to_dict(self):
        # Method to include computed field in dictionary representation
        print("[based]", self.__dict__)
        return {
            **self.dict(),
            "template": self.template()
        }
