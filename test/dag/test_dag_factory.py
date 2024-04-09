import unittest
import unittest.mock

from src.dag.dag_factory import DAGFactory


def test_dag_factory():
    mock_file_content = """
        [{"name": "Earth","surfaceTemperature": 288},
        {"name": "Mars", "surfaceTemperature": 260}]
        """
    with unittest.mock.patch(
        "builtins.open",
        new=unittest.mock.mock_open(read_data=mock_file_content),
        create=True,
    ) as file_mock:
        assert DAGFactory.read_etl_description(file_path="/dev/null")
