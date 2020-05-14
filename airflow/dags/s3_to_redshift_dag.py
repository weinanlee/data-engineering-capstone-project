from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime, timedelta


from airflow.operators import ExtractionFromSASOperator



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

extract_sas_data_operator = ExtractionFromSASOperator(
	task_id ='Extract_data_from_SAS_save_as_csv_in_s3bucket',
	dag=dag,
	s3_bucket = 'uda-capstone-data',
  s3_load_prefix = 'sas_data',
  s3_save_prefix = 'csv_data',
  file_name = 'I94_SAS_Labels_Descriptions.SAS')


start_operator = DummyOperator(task_id='Begin_execution', dag=dag)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)


start_operator >> extract_sas_data_operator
extract_sas_data_operator >> end_operator