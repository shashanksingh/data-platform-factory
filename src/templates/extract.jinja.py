# type: ignore
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator

with TaskGroup(group_id='extract') as extract:
    def load_task(**kwargs):
        print(f"Loading data from extract")

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load_task,
        op_kwargs={'params': {'destination': '{destination}'}},
        dag=dag
    )