from src.extract.extract import Extract


class PostgresExtract(Extract):

    connection_name:str
    database_name:str
    table_name:str
    sync_type:str = "FULL"
