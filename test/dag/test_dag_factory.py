import unittest
import unittest.mock

from src.dag.dag_factory import DAGFactory


def test_dag_factory():
    mock_file_content = """
            [Extract]
            source="postgres"
            [Load]
            destination="redshift"
        """
    with unittest.mock.patch(
        "builtins.open",
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True,
    ) as file_mock:
        assert DAGFactory.read_etl_description(file_path="/dev/null")
        assert file_mock.call_count == 1
