from ..extract.extract import Extract
from ..load.load import Load
from ..transform.transform import Transform
from ..report.report import Report
from ..wait.wait import Wait
from dag_description import DAGDescription
import toml


class DAGFactory:
    @staticmethod
    def create_extract(config: dict) -> Extract:
        return Extract(**config)

    @staticmethod
    def create_load(config: dict) -> Load:
        return Load(**config)

    @staticmethod
    def create_transform(configs: list) -> list:
        transforms = []
        # for transform_config in configs:
        #     if "dedup" in transform_config:
        #         transforms.append(DedupTransform())
        #     elif "drop_na" in transform_config:
        #         transforms.append(DropNATransform())
        return transforms

    @staticmethod
    def create_report(configs: list) -> Report:
        pass

    @staticmethod
    def create_wait(configs: list) -> Wait:
        pass

    @staticmethod
    def read_etl_description(file_path: str) -> DAGDescription:
        factory = DAGFactory()
        with open(file_path, 'r') as file:
            data = toml.load(file)

        extract = factory.create_extract(data.get('Extract', {}))
        transforms = factory.create_transform(data.get('Transform', []))
        load = factory.create_load(data.get('Load', {}))
        report = factory.create_report(data.get('Report',{}))
        wait = factory.create_wait(data.get('Wait', {}))

        return DAGDescription(extract=extract, transforms=transforms, load=load, report=report, wait=wait)
