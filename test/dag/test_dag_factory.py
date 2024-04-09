import unittest
import unittest.mock
import pprint

from src.dag.dag_description import DAGDescription
from src.dag.dag_factory import DAGFactory
from src.extract.extract import Extract
from src.load.load import Load


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
        # given
        extract = Extract(source="postgres")
        load = Load(destination="redshift")

        # when
        dagfactory = DAGFactory.read_etl_description(file_path="/dev/null")
        # then
        assert dagfactory == DAGDescription(extract=extract, load=load)
        assert file_mock.call_count == 1
        pprint.pprint(dagfactory)
