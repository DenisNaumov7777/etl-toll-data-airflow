# import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email import EmailOperator
from airflow.utils.dates import days_ago

#defining DAG arguments

default_args = {
    'owner': 'Denis',
    'start_date': days_ago(0),
    'email': ['Denis_Naumov@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# define the DAG

dag = DAG(
    dag_id='ETL_toll_data',
    default_args=default_args,
    description='Apache Airflow Final Assignment',
    schedule_interval=timedelta(days=1),
)

# define a task with BashOperator

unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz ' \
                 '-C /home/project/airflow/dags/finalassignment',
    dag=dag,
)

extract_data_from_csv = BashOperator(
    task_id='extract_data_from_csv',
    bash_command='cut -d"," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > ' \
                 '/home/project/airflow/dags/finalassignment/csv_data.csv',
 

   dag=dag,
)

extract_data_from_tsv = BashOperator(
    task_id='extract_data_from_tsv',
    bash_command="cut -d$'\t' -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv > "
                 "/home/project/airflow/dags/finalassignment/tsv_data.csv",
    dag=dag,
)

extract_data_from_fixed_width = BashOperator(
    task_id='extract_data_from_fixed_width',
    bash_command="cut -c59-67 /home/project/airflow/dags/finalassignment/payment-data.txt > "
                 "/home/project/airflow/dags/finalassignment/fixed_width_data.csv",
    dag=dag,
)


consolidate_data = BashOperator(
    task_id='consolidate_data',
    bash_command="paste -d ',' /home/project/airflow/dags/finalassignment/csv_data.csv " \
                 "/home/project/airflow/dags/finalassignment/tsv_data.csv " \
                 "/home/project/airflow/dags/finalassignment/fixed_width_data.csv > " \
                 "/home/project/airflow/dags/finalassignment/extracted_data.csv",
    dag=dag,
)

transform_data = BashOperator(
    task_id='transform_data',
    bash_command="tr '[:lower:]' '[:upper:]' < " \
                 "/home/project/airflow/dags/finalassignment/extracted_data.csv > " \
                 "/home/project/airflow/dags/finalassignment/transformed_data.csv",
    dag=dag,
)

unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data