from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from kafka_producer.kafka_producer import kafka_txn_producer


default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2025, 1, 1, 00, 00)
}

with DAG('prcess_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='straming_generated_data',
        python_callable=kafka_txn_producer,
        dag=dag
    )