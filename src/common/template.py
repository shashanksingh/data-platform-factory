from abc import ABC, abstractmethod


class Template(ABC):
    @property
    @abstractmethod
    def template(self):
        """The template """
