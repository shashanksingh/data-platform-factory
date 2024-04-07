from ..extract.extract import Extract
from ..load.load import Load
from ..transform.transform import Transform
from ..report.report import Report
from ..wait.wait import Wait
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
