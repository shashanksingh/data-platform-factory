from typing import Dict
from jinja2 import Environment, FileSystemLoader
import toml

from src.dag.dag import DAG
from src.dag.dag_description import DAGDescription
from src.extract.extract import Extract
from src.dag.dag_description_builder import DAGDescriptionBuilder
from src.extract.extract_factory import ExtractFactory
from src.load.load import Load
from src.load.load_factory import LoadFactory
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGFactory:
    @staticmethod
    def create_dag(config: Dict) -> DAG:
        return DAG(**config)

    @staticmethod
    def create_extract(config: Dict) -> Extract:
        ExtractFactory.auto_register_classes()
        return ExtractFactory.create(extract_type=config.get("type"), **config)

    @staticmethod
    def create_load(config: Dict) -> Load:
        LoadFactory.auto_register_classes()
        return LoadFactory.create(load_type=config.get("type"), **config)

    @staticmethod
    def create_transform(configs: Dict) -> Transform:
        return Transform(**configs)

    @staticmethod
    def create_report(configs: Dict) -> Report:
        return Report(**configs)

    @staticmethod
    def create_wait(configs: Dict) -> Wait:
        return Wait(**configs)

    @staticmethod
    def read_etl_description(file_path: str) -> DAGDescription:
        factory = DAGFactory()
        with open(file_path, "r") as file:
            data = toml.loads(file.read())

        dag: DAG = factory.create_dag(data.get("DAG", {}))
        extract: Extract = factory.create_extract(data.get("Extract", {}))
        load: Load = factory.create_load(data.get("Load", {}))

        dag_description_builder = DAGDescriptionBuilder()
        (dag_description_builder.with_dag(dag).with_extract(extract).with_load(load))

        if data.get("Report"):
            dag_description_builder.with_report(data.get("Report"))  # type: ignore
        if data.get("Wait"):
            dag_description_builder.with_wait(data.get("Wait"))  # type: ignore
        if data.get("Transform"):
            dag_description_builder.with_transforms(data.get("Transform"))  # type: ignore
        return dag_description_builder.build()

    @staticmethod
    def render(dag_description: DAGDescription) -> str:
        env = Environment(loader=FileSystemLoader("src/templates"))
        template = env.get_template("base.py.jinja")

        output = template.render(dag_description=dag_description.convert_to_dict())
        return output

    @staticmethod
    def generate_dag_name(dag_description: DAGDescription) -> str:
        return f"load_from_{str(dag_description.extract)}_to_{str(dag_description.load)}"
