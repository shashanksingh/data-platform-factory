import unittest
import unittest.mock
import pytest
from src.dag.dag_description import DAGDescription
from src.dag.dag_factory import DAGFactory
from src.extract.extract import Extract
from src.load.load import Load


@pytest.mark.parametrize(
    "mock_file_content,expected_object",
    [
        (
            """
            [Extract]
            source="postgres"
            [Load]
            destination="redshift"
        """,
            DAGDescription(
                extract=Extract(source="postgres"), load=Load(destination="redshift")
            ),
        ),
    ],
    ids=["extract-load", ],
)
def test_dag_factory(mock_file_content, expected_object):
    with unittest.mock.patch(
        "builtins.open",
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True,
    ) as file_mock:
        # given-when
        dagfactory = DAGFactory.read_etl_description(file_path="/dev/null")
        # then
        assert dagfactory == expected_object
        assert file_mock.call_count == 1
