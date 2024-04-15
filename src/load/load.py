from pydantic import BaseModel, ConfigDict
import abc


class Load(BaseModel):
    model_config = ConfigDict(extra="forbid")

    destination: str

    @property
    @abc.abstractmethod
    def template(self):
        """ The template for the extract"""

    def __str__(self):
        return self.destination
