from pydantic import computed_field

from src.load.load import Load


class Redshift(Load):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"
    type: str = "postgres"

    @computed_field(return_type="str")
    def s3_bucket(self) -> str:
        return "s3://data-platform-factory"  # TODO needs to be figured out

    @computed_field(return_type=str)
    def template(self):
        return (
            f"        RedshiftSQLOperator(\n"
            f'            task_id="load_{self.database_name}_{self.table_name}",\n'
            f'            sql="COPY sales\n'
            f"            FROM {self.s3_bucket}\n"
            f"            DELIMITER '\t' \n"
            f"            TIMEFORMAT 'MM/DD/YYYY HH:MI:SS' \n"
            f"            REGION 'us-east-1'\n"
            f"            IAM_ROLE default; \n"
            f'            ",\n'
            f"        )\n"
            f"    "
        )
