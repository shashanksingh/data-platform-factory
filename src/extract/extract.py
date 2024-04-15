from typing import Dict, Any

from pydantic import ConfigDict

from src.common.base_dag_factory_model import BaseDAGFactoryModel


class Extract(BaseDAGFactoryModel):
    model_config = ConfigDict(extra="forbid")
    conn_id: str

    def __str__(self):
        return self.conn_id


class ExtractFactoryMeta(type):
    _registry: Dict = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name != "Extract":
            cls._registry[name.lower()] = new_class
        return new_class

    @classmethod
    def create(cls, extract_type):
        extract_class = cls._registry.get(extract_type.lower())
        if extract_class:
            return extract_class()
        else:
            raise ValueError(f"Unknown shape type: {extract_type}")

    @classmethod
    def register_child(cls, extract_child_name: str, extract_child_class: Any) -> None:
        cls._registry[extract_child_name] = extract_child_class


class ExtractFactory(metaclass=ExtractFactoryMeta):
    pass
