# type: ignore
from __future__ import annotations
import pendulum
from airflow.models.dag import DAG


dag1 = DAG(
    dag_id="example_branch_datetime_operator",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
    schedule="@daily",
)

{% if 'extract' in dag_definition %}
    data.extract.template
{% endif %}

# extract >> wait>> transform >> wait >> load
# [END howto_branch_datetime_operator]
