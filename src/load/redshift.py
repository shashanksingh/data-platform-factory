from typing import Optional
from pydantic import computed_field
from src.extract.load import Load


class Redshift(Load):
    conn_id: str
    database_name: str
    table_name: str
    sync_type: str = "FULL"
    type: str = "postgres"

    @computed_field(return_type="str")
    def s3_bucket(self) -> str:
        return 's3://data-platform-factory'   # TODO needs to be figured out

    @computed_field(return_type=str)
    def template(self):
        return f"""
        RedshiftSQLOperator(
            task_id="load_{self.database_name}_{self.table_name}",
            sql="COPY sales
            FROM {self.s3_bucket}
            DELIMITER '\t' 
            TIMEFORMAT 'MM/DD/YYYY HH:MI:SS' 
            REGION 'us-east-1'
            IAM_ROLE default; 
            ",
        )
    """
