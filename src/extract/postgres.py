from src.common.template import Template
from src.extract.extract import Extract, ExtractFactory


class Postgres(Extract, Template):
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



ExtractFactory.register_child(
    extract_child_name="postgres", extract_child_class=Postgres
)