from src.extract.extract import Extract


class Postgres(Extract):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"
    type: str = "postgres"
