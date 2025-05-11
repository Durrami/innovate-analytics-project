from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))

# Import functions from project
from src.data_processing import extract_data, transform_data, load_data
from src.model import train_model
from src.utils import create_sample_data

default_args = {
    'owner': 'innovate_analytics',
    'depends_on_past': False,
    'start_date': datetime(2025, 5, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ml_pipeline',
    default_args=default_args,
    description='Complete ML pipeline for Innovate Analytics',
    schedule_interval=timedelta(days=1),
)

t0 = PythonOperator(
    task_id='create_sample_data',
    python_callable=create_sample_data,
    dag=dag,
)

t1 = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

t2 = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

t3 = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

t4 = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag,
)

t0 >> t1 >> t2 >> t3 >> t4