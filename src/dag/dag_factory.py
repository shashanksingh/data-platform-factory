from typing import List

from src.dag.dag_description import DAGDescription

import toml
from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGFactory:
    @staticmethod
    def create_extract(config: dict) -> Extract:
        return Extract(**config)

    @staticmethod
    def create_load(config: dict) -> Load:
        return Load(**config)

    @staticmethod
    def create_transform(configs: dict) -> Transform:
        return Transform(**configs)

    @staticmethod
    def create_report(configs: dict) -> Report:
        return Report(**configs)

    @staticmethod
    def create_wait(configs: dict) -> Wait:
        return Wait(**configs)

    @staticmethod
    def read_etl_description(file_path: str) -> DAGDescription:
        factory = DAGFactory()
        with open(file_path, "r") as file:
            data = toml.loads(file.read())

        extract = factory.create_extract(data.get("Extract", {}))
        # TODO fix transforms
        transforms: Transform = (
            factory.create_transform(data.get("Transform"))
            if data.get("Transform")
            else None
        )
        load: Load = factory.create_load(data.get("Load", {}))
        report: Report = (
            factory.create_report(data.get("Report")) if data.get("Report") else None
        )
        wait: Wait = factory.create_wait(data.get("Wait")) if data.get("Wait") else None

        return DAGDescription(
            extract=extract, transforms=None, load=load, report=report, wait=wait
        )
