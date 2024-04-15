from src.extract.extract import Extract


class PostgresExtract(Extract):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"

    @property
    def template(self):
        return f"""PostgresOperator(
            task_id="extract_{self.database_name}_{self.table_name}",
            sql="SELECT * from {self.database_name}.{self.table_name};",
        )"""


Extract.register_handler(PostgresExtract)
