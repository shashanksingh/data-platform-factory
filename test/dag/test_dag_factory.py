import unittest
import unittest.mock
import pytest

from src.dag.dag import DAG
from src.dag.dag_description import DAGDescription
from src.dag.dag_factory import DAGFactory
from src.extract.extract import Extract
from src.load.load import Load
from src.report.report import Report
from src.transform.transform import Transform
from src.wait.wait import Wait


@pytest.mark.parametrize(
    "mock_file_content,expected_object",
    [
        (
            """
                [DAG]
                type="rdbms-to-dwh"
                [Extract]
                name = "postgres"
                [Load]
                destination = "redshift"

        """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Extract(source="postgres"),
                load=Load(destination="redshift"),
            ),
        ),
        (
            """
                [DAG]
                type="rdbms-to-dwh"
                [Extract]
                name="postgres"
                [Wait]
                after_source="catalog.table"
                [Load]
                destination="redshift"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Extract(source="postgres"),
                load=Load(destination="redshift"),
                wait=Wait(after_source="catalog.table"),
            ),
        ),
        (
            """
                [DAG]
                type="rdbms-to-dwh"
                [Extract]
                name="postgres"
                [Load]
                destination="redshift"
                [Report]
                name="slack"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Extract(source="postgres"),
                load=Load(destination="redshift"),
                report=Report(source="slack"),
            ),
        ),
        (
            """[DAG]
                type="rdbms-to-dwh"
                [Extract]
                name="postgres"
                [Load]
                destination="redshift"
                [Transform]
                name="dedup"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Extract(source="postgres"),
                load=Load(destination="redshift"),
                transforms=Transform(name="dedup"),
            ),
        ),
        (
            """[DAG]
                type="rdbms-to-dwh"
                    [Extract]
                    name="postgres"
                    [Wait]
                    after_source="catalog.table"
                    [Load]
                    destination="redshift"
                    [Transform]
                    name="dedup"
                """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Extract(source="postgres"),
                wait=Wait(after_source="catalog.table"),
                load=Load(destination="redshift"),
                transforms=Transform(name="dedup"),
            ),
        ),
    ],
    ids=[
        "extract-load",
        "extract-wait-load",
        "extract-load-report",
        "extract-transform-load",
        "extract-wait-transform-load",
    ],
)
def test_dag_factory(mock_file_content, expected_object):
    with unittest.mock.patch(
        "builtins.open",
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True,
    ) as file_mock:
        # given-when
        dag_factory = DAGFactory.read_etl_description(file_path="/dev/null")
        # then
        assert dag_factory == expected_object
        assert file_mock.call_count == 1
