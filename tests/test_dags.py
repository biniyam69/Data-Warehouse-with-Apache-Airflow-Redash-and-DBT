import pytest
import pandas as pd
import sys
import os
from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.utils.state import State
from werkzeug.local import LocalProxy



current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# add the parent directory containing the module to the python path
sys.path.append(project_root)

@pytest.fixture
def dag_bag():
    return DagBag(dag_folder='/home/biniyam/dwh-project-UAV/airflow/dags/', include_examples=False)

def test_extract_load_dag(dag_bag):
    dag_id = 'extract_load'
    assert dag_id in dag_bag.dags, f'DAG {dag_id} not found'

def test_el_dag_tasks(dag_bag):
    dag_id = 'extract_load'
    dag = dag_bag.get_dag(dag_id)
    assert dag is not None, f"DAG '{dag_id}' should not be None"

    task_ids = [task.task_id for task in dag.tasks]
    for task_id in task_ids:
        assert dag.get_task(task_id) is not None, f"Task '{task_id}' missing from DAG '{dag_id}'"

def test_el_dag_dependencies(dag_bag):
    dag_id = 'extract_load'
    dag = dag_bag.get_dag(dag_id)
    assert dag is not None, f"DAG '{dag_id}' should not be None"

    dependencies = {
        'read_data': ['create_table'],
        'create_table': ['insert_vehicles_to_table', 'insert_traj_to_table'],
        'insert_vehicles_to_table': [],
        'insert_traj_to_table': []
    }

    for task_id, upstream_list in dependencies.items():
        task = dag.get_task(task_id)
        assert task is not None, f"Task '{task_id}' missing from DAG '{dag_id}'"
        upstream_task_ids = [task.task_id for task in task.upstream_list]
        assert upstream_task_ids == upstream_list, f"Task '{task_id}' in DAG '{dag_id}' has incorrect upstream list"
    
def test_el_dag_execution(dag_bag):
    dag_id = 'extract_load'
    dag = dag_bag.get_dag(dag_id)
    assert dag is not None, f"DAG '{dag_id}' should not be None"

    task_ids = [task.task_id for task in dag.tasks]

    for task_id in task_ids:
        task = dag.get_task(task_id)
        assert task.state == State.NONE, f"Task '{task_id}' in DAG '{dag_id}' should be in NONE state"

    dag.run(start_date=days_ago(1), end_date=days_ago(0), dry_run=True, local=True)

    for task_id in task_ids:
        task = dag.get_task(task_id)
        assert task.state == State.SUCCESS, f"Task '{task_id}' in DAG '{dag_id}' failed"