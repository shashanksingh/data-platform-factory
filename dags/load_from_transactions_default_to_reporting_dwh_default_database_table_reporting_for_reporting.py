# type: ignore
# flake8: noqa
from __future__ import annotations
import pendulum
from airflow.models.dag import DAG

with DAG(
    dag_id="transactions_default_to_reporting_dwh_default",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=['generated-dags'],
    schedule="@hourly",
) as dag:


    from airflow.utils.task_group import TaskGroup
    from airflow.operators.python import PythonOperator

    with TaskGroup(group_id="extract") as extract:

        def load_task(**kwargs):
            print(f"Loading data from extract")

        load_task = PythonOperator(
            task_id="load_task",
            python_callable=load_task,
            op_kwargs={"params": {"destination": "{destination}"}},
            dag=dag,
        )

        from airflow.providers.postgres.operators.postgres import PostgresOperator

        PostgresOperator(
                task_id="extract_database_table",
                sql="SELECT * from database.table;",
            )




    from airflow.utils.task_group import TaskGroup
    from airflow.operators.python import PythonOperator

    with TaskGroup(group_id="load") as extract:

        def load_task(**kwargs):
            print(f"loading data into destination")

        load_task = PythonOperator(
            task_id="load_task",
            python_callable=load_task,
            op_kwargs={"params": {"destination": "{destination}"}},
            dag=dag,
        )

        from airflow.providers.amazon.aws.operators.redshift import RedshiftSQLOperator

        RedshiftSQLOperator(
            task_id="load_database_table_reporting",
            sql="""COPY sales
            FROM s3://data-platform-factory
            DELIMITER '	'
            TIMEFORMAT 'MM/DD/YYYY HH:MI:SS'
            REGION 'us-east-1'
            IAM_ROLE default;
            """,
        )
    








# extract >> wait>> transform >> wait >> load
# [END howto_branch_datetime_operator]