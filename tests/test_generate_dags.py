import unittest
import pytest

from src.generate_dags import generate_dags
from click.testing import CliRunner


@pytest.mark.parametrize(
    "mock_file_content, expected_output",
    [
        (
            """
            [DAG]
            schedule = "@continuous"
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
            """Hello definitions/!!\n""",
        ),
    ],
    ids=["extract-load"],
)
def test_generate_dags(mock_file_content, expected_output):
    # This makes sure we don't actually generate a build python file while unittesting
    with unittest.mock.patch(
        "builtins.open",
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True,
    ) as _:
        runner = CliRunner()
        result = runner.invoke(generate_dags, ["--directory", "definitions/"])
        assert result.exit_code == 0
        assert result.output == expected_output
