import os
from typing import Dict, Any

from src.load.redshift import Redshift


class LoadFactoryMeta(type):
    _registry: Dict = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        if name != "Extract":
            cls._registry[name.lower()] = new_class
        return new_class

    @classmethod
    def create(cls, load_type, **config):
        load_class = cls._registry.get(load_type.lower())
        if load_class:
            return load_class(**config)
        else:
            raise ValueError(f"Unknown Load Type: {load_type}")

    @classmethod
    def register_child(cls, load_child_name: str, load_child_class: Any) -> None:
        cls._registry[load_child_name] = load_child_class

    @classmethod
    def auto_register_classes(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for file_name in os.listdir(current_dir):
            if (
                file_name.endswith(".py")
                and file_name != "__init__.py"
                and file_name != "load_factory.py"
            ):
                # module_name = file_name[:-3]  # Remove '.py' extension
                # TODO
                # module = __import__(module_name)
                # for name, obj in inspect.getmembers(module):
                #     if inspect.isclass(obj) :
                name = "Redshift"
                cls._registry[name.lower()] = Redshift


class LoadFactory(metaclass=LoadFactoryMeta):
    pass
