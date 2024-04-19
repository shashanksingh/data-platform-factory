from pydantic import computed_field

from src.load.load import Load


class Redshift(Load):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"
    type: str = "redshift"

    @computed_field(return_type="str")
    def s3_bucket(self) -> str:
        return "s3://data-platform-factory"  # TODO needs to be figured out

    def __str__(self):
        return f"{self.conn_id}_{self.database_name}_{self.table_name}"

    @computed_field(return_type=str)
    def task_id(self):
        return f"load_{self.database_name}_{self.table_name}"