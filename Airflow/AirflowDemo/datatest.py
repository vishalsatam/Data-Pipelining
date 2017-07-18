import airflow
from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'manasi',
    'depends_on_past': False,
    'start_date': datetime(2016, 4, 15),
    'email': ['manasidalvi14@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG('datafile', default_args=default_args)


def task_read13():
  print("hello from task13 read data")
  #query="https://data.colorado.gov/resource/tv8u-hswn.json"
  data_2013=pd.read_json("https://data.policefoundation.org/resource/jhvd-4583.json")
  data_2013.to_csv('/home/manasi/outputcsv/data_2013.csv')

def task_read12():
  print("hello from task12 read data")
  #query="https://data.colorado.gov/resource/tv8u-hswn.json"
  data_2012=pd.read_json("https://data.policefoundation.org/resource/fgcx-vmf9.json")
  data_2012.to_csv('/home/manasi/outputcsv/data_2012.csv')

 
def task_merge():
   print("tasks 2012")
   data_2012=pd.read_csv('/home/manasi/outputcsv/data_2012.csv')
   year2012=data_2012['ward'].value_counts(sort=True, ascending=True).to_frame() #2012 arrests by ward
   print("tasks 2013")
   data_2013=pd.read_csv('/home/manasi/outputcsv/data_2012.csv')
   year2013=data_2013['ward'].value_counts(sort=True, ascending=True).to_frame() #2013 arrests by ward
   m=pd.concat([year2012,year2013],axis=1)
   m.columns=['year2012','year2013']
   m.to_csv('/home/manasi/outputcsv/merge/mdata.csv')


t1 = BashOperator(
    task_id='read_json_2012',
    python_callable=task_read12(),
    bash_command='python3 ~/airflow/dags/datatest.py',
    dag=dag)

t2 = BashOperator(
    task_id='read_json_2013',
    python_callable=task_read13(),
    bash_command='python3 ~/airflow/dags/datatest.py',
    dag=dag)

t3 = BashOperator(
    task_id='merge',
    python_callable=task_merge(),
    bash_command='python3 ~/airflow/dags/datatest.py',
    dag=dag)

t3.set_upstream(t1)
t3.set_upstream(t2)

