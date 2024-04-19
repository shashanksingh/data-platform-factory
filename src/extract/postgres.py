from pydantic import computed_field

from src.extract.extract import Extract


class Postgres(Extract):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"
    type: str = "postgres"

    @computed_field(return_type=str)
    def task_id(self):
        return f"extract_{self.database_name}_{self.table_name}"
