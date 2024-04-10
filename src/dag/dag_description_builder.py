from src.dag.dag_description import DAGDescription
from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


class DAGDescriptionBuilder:
    def __init__(self):
        self._extract = None
        self._transforms = None
        self._load = None
        self._report = None
        self._wait = None

    def with_extract(self, extract: Extract):
        self._extract = extract
        return self

    def with_transforms(self, transforms: Transform):
        self._transforms = transforms
        return self

    def with_load(self, load: Load):
        self._load = load
        return self

    def with_report(self, report: Report):
        self._report = report
        return self

    def with_wait(self, wait: Wait):
        self._wait = wait
        return self

    def build(self):
        return DAGDescription(
            extract=self._extract,
            transforms=self._transforms,
            load=self._load,
            report=self._report,
            wait=self._wait,
        )
