from typing import Dict
from jinja2 import Environment, BaseLoader, FileSystemLoader
import toml
from src.dag.dag_description import DAGDescription
from src.extract.extract import Extract
from src.dag.dag_description_builder import DAGDescriptionBuilder
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGFactory:
    @staticmethod
    def create_extract(config: dict) -> Extract:
        return Extract(**config)

    @staticmethod
    def create_load(config: Dict) -> Load:
        return Load(**config)

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

        extract: Extract = factory.create_extract(data.get("Extract", {}))
        load: Load = factory.create_load(data.get("Load", {}))

        dag_description_builder = DAGDescriptionBuilder()
        dag_description_builder.with_extract(extract).with_load(load)

        if data.get("Report"):
            dag_description_builder.with_report(data.get("Report"))  # type: ignore
        if data.get("Wait"):
            dag_description_builder.with_wait(data.get("Wait"))  # type: ignore
        if data.get("Transform"):
            dag_description_builder.with_transforms(data.get("Transform"))  # type: ignore
        return dag_description_builder.build()

    @staticmethod
    def render(dag_description: DAGDescription) -> str:
        env = Environment(loader=FileSystemLoader('src.templates'))
        template = env.get_template('child_template.html')
        output = template.render(dag_description)
        print(output)
        return output