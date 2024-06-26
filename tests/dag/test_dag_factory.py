import unittest
import unittest.mock
import pytest

from src.dag.dag import DAG
from src.dag.dag_description import DAGDescription
from src.dag.dag_factory import DAGFactory
from src.extract.postgres import Postgres
from src.load.redshift import Redshift
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
                conn_id = "transactions_default"
                type="postgres"
                database_name="database"
                table_name="table"
                [Load]
                conn_id = "transactions_dwh_default"
                type="redshift"
                database_name="database"
                table_name="table"

        """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Postgres(
                    conn_id="transactions_default",
                    database_name="database",
                    table_name="table",
                ),
                load=Redshift(
                    conn_id="transactions_dwh_default",
                    database_name="database",
                    table_name="table",
                ),
            ),
        ),
        (
            """
                [DAG]
                type="rdbms-to-dwh"
                [Extract]
                conn_id = "transactions_default"
                type="postgres"
                database_name="database"
                table_name="table"
                [Wait]
                after_source="catalog.table"
                [Load]
                conn_id = "transactions_dwh_default"
                type="redshift"
                database_name="database"
                table_name="table"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Postgres(
                    conn_id="transactions_default",
                    database_name="database",
                    table_name="table",
                ),
                load=Redshift(
                    conn_id="transactions_dwh_default",
                    database_name="database",
                    table_name="table",
                ),
                wait=Wait(after_source="catalog.table"),
            ),
        ),
        (
            """
                [DAG]
                type="rdbms-to-dwh"
                [Extract]
                conn_id = "transactions_default"
                type="postgres"
                database_name="database"
                table_name="table"
                [Load]
                conn_id = "transactions_dwh_default"
                type="redshift"
                database_name="database"
                table_name="table"
                [Report]
                source="slack"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Postgres(
                    conn_id="transactions_default",
                    database_name="database",
                    table_name="table",
                ),
                load=Redshift(
                    conn_id="transactions_dwh_default",
                    database_name="database",
                    table_name="table",
                ),
                report=Report(source="slack"),
            ),
        ),
        (
            """ [DAG]
                type="rdbms-to-dwh"
                [Extract]
                conn_id = "transactions_default"
                type="postgres"
                database_name="database"
                table_name="table"
                [Load]
                conn_id = "transactions_dwh_default"
                type="redshift"
                database_name="database"
                table_name="table"
                [Transform]
                name="dedup"
            """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Postgres(
                    conn_id="transactions_default",
                    database_name="database",
                    table_name="table",
                ),
                load=Redshift(
                    conn_id="transactions_dwh_default",
                    database_name="database",
                    table_name="table",
                ),
                transforms=Transform(name="dedup"),
            ),
        ),
        (
            """[DAG]
                    type="rdbms-to-dwh"
                    [Extract]
                    conn_id = "transactions_default"
                    type="postgres"
                    database_name="database"
                    table_name="table"
                    [Wait]
                    after_source="catalog.table"
                    [Load]
                    conn_id = "transactions_dwh_default"
                    type="redshift"
                    database_name="database"
                    table_name="table"
                    [Transform]
                    name="dedup"
                """,
            DAGDescription(
                dag=DAG(type="rdbms-to-dwh"),
                extract=Postgres(
                    conn_id="transactions_default",
                    database_name="database",
                    table_name="table",
                ),
                wait=Wait(after_source="catalog.table"),
                load=Redshift(
                    conn_id="transactions_dwh_default",
                    database_name="database",
                    table_name="table",
                ),
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
