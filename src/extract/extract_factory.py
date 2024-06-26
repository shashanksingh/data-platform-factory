import os
from typing import Dict, Any

from src.extract.postgres import Postgres


class ExtractFactoryMeta(type):
    _registry: Dict = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name != "Extract":
            cls._registry[name.lower()] = new_class
        return new_class

    @classmethod
    def create(cls, extract_type, **config):
        extract_class = cls._registry.get(extract_type.lower())
        if extract_class:
            return extract_class(**config)
        else:
            raise ValueError(f"Unknown Extract Type: {extract_type}")

    @classmethod
    def register_child(cls, extract_child_name: str, extract_child_class: Any) -> None:
        cls._registry[extract_child_name] = extract_child_class

    @classmethod
    def auto_register_classes(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for file_name in os.listdir(current_dir):
            if (
                file_name.endswith(".py")
                and file_name != "__init__.py"
                and file_name != "extract_factory.py"
            ):
                # module_name = file_name[:-3]  # Remove '.py' extension
                # TODO
                # module = __import__(module_name)
                # for name, obj in inspect.getmembers(module):
                #     if inspect.isclass(obj) :
                name = "Postgres"
                cls._registry[name.lower()] = Postgres


class ExtractFactory(metaclass=ExtractFactoryMeta):
    pass
