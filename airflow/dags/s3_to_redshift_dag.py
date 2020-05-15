from airflow.operators.dummy_operator import DummyOperator
from airflow import DAG
from datetime import datetime, timedelta


from airflow.operators import (ExtractionFromSASOperator, CreateTableOperator)
from helpers import SqlQueries


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

create_immigration_table = CreateTableOperator(
  task_id = 'Create_immigration_table',
  dag=dag,
  table = 'immigration',
  create_sql_stmt = SqlQueries.immigrant_table_create,
  drop_sql_stmt = SqlQueries.drop_table
  )

create_i94cit_i94res_table = CreateTableOperator(
  task_id = 'Create_i94cit_i94res_table',
  dag=dag,
  table = 'i94cit_i94res',
  create_sql_stmt = SqlQueries.i94cit_i94res_table_create,
  drop_sql_stmt = SqlQueries.drop_table
  )

create_i94mode_table = CreateTableOperator(
  task_id = 'Create_i94mode_table',
  dag=dag,
  table = 'i94mode',
  create_sql_stmt = SqlQueries.i94mode_table_create,
  drop_sql_stmt = SqlQueries.drop_table
  )

create_i94addr_table = CreateTableOperator(
  task_id = 'Create_i94addr_table',
  dag=dag,
  table = 'i94addr',
  create_sql_stmt = SqlQueries.i94addr_table_create,
  drop_sql_stmt = SqlQueries.drop_table
)

create_i94visa_table = CreateTableOperator(
  task_id = 'Create_i94visa_table',
  dag=dag,
  table = 'i94visa',
  create_sql_stmt = SqlQueries.i94visa_table_create,
  drop_sql_stmt = SqlQueries.drop_table
  )

start_operator = DummyOperator(task_id='Begin_execution', dag=dag)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)


start_operator >> extract_sas_data_operator

extract_sas_data_operator >> create_immigration_table
extract_sas_data_operator >> create_i94cit_i94res_table
extract_sas_data_operator >> create_i94mode_table
extract_sas_data_operator >> create_i94addr_table
extract_sas_data_operator >> create_i94visa_table

create_immigration_table >> end_operator


