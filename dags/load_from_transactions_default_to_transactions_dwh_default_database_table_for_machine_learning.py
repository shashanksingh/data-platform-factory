# type: ignore
# flake8: noqa
from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id="transactions_default_to_transactions_dwh_default",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=['generated-dags'],
    schedule="@continuous",
    max_active_runs=1,
) as dag:


    with TaskGroup(group_id="extract") as extract:
        from airflow.operators.python import PythonOperator


        def load_task(**kwargs):
            print(f"Loading data from extract")

        load_task = PythonOperator(
            task_id="load_task",
            python_callable=load_task,
            op_kwargs={"params": {"destination": "{destination}"}},
            dag=dag,
        )

        PostgresOperator(
                    task_id="extract_{self.database_name}_{self.table_name}",
                    sql="SELECT * from {self.database_name}.{self.table_name};",
                )



    with TaskGroup(group_id="load") as load:
        from airflow.operators.python import PythonOperator



        def load_task(**kwargs):
            print(f"loading data into destination")

        load_task = PythonOperator(
            task_id="load_task",
            python_callable=load_task,
            op_kwargs={"params": {"destination": "{destination}"}},
            dag=dag,
        )

        PostgresOperator(
                        task_id="load_{self.database_name}_{self.table_name}",
                        sql="select 1"
                    )











        extract >> load



