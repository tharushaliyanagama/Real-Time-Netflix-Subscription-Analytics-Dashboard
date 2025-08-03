from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def batch_process():
    import subprocess
    subprocess.run(['python', 'scripts/batch_processing.py'])

def stream_process():
    import subprocess
    subprocess.run(['python', 'scripts/stream_processing.py'])

with DAG('netflix_pipeline', start_date=datetime(2025, 8, 1), schedule_interval='@hourly') as dag:
    batch_task = PythonOperator(task_id='batch_process', python_callable=batch_process)
    stream_task = PythonOperator(task_id='stream_process', python_callable=stream_process)
    batch_task >> stream_task