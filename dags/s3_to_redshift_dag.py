from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'weinanli',
    'start_date': datetime(2019, 1, 12),
    'depends_on_past': False,
    'retries': 0,
    'retry_delay': 300,
    'email_on_retry': False
}

dag = DAG('S3_to_redshift_dag',
          default_args=default_args,
          description='Load and transform data in Redshift with Airflow',
          schedule_interval='@hourly',
          catchup=False)


start_operator = DummyOperator(task_id='Begin_execution', dag=dag)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)