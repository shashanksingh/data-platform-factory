from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.datetime import BranchDateTimeOperator
from airflow.operators.empty import EmptyOperator

dag1 = DAG(
    dag_id="example_branch_datetime_operator",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
    schedule="@daily",
)

# [START howto_branch_datetime_operator]
empty_task_11 = EmptyOperator(task_id="date_in_range", dag=dag1)
empty_task_21 = EmptyOperator(task_id="date_outside_range", dag=dag1)

cond1 = BranchDateTimeOperator(
    task_id="datetime_branch",
    follow_task_ids_if_true=["date_in_range"],
    follow_task_ids_if_false=["date_outside_range"],
    target_upper=pendulum.datetime(2020, 10, 10, 15, 0, 0),
    target_lower=pendulum.datetime(2020, 10, 10, 14, 0, 0),
    dag=dag1,
)

# Run empty_task_11 if cond1 executes between 2020-10-10 14:00:00 and 2020-10-10 15:00:00
cond1 >> [empty_task_11, empty_task_21]
# [END howto_branch_datetime_operator]


