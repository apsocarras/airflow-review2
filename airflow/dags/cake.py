import os 
from datetime import datetime
from airflow import DAG
from airflow.decorators import dag, task
from airflow.sensors.filesystem import FileSensor 
from airflow.hooks.filesystem import FSHook

# ## Assignment: 
# Uses a file sensor to check whether the votes.csv file has been uploaded to the data/ folder of this repository.
# Has a task that reads each row in votes.csv, and checks whether that value is in the flavors_choices list defined above. 
# If it is, append it to a new list called valid_votes. This task should return the valid_votes list.
# In another task, use a Python function that takes a list as an argument, and prints the item that appear the most times in that list.
# Pass the return_value XCom from the first task as an argument to the second task.
# Use decorators to define the tasks.

FLAVORS = ["lemon", "vanilla", "chocolate",
 "pistachio", "strawberry", "confetti", "caramel", "pumpkin", "rose"]

FILENAME = "votes.csv"

data_fs = FSHook(conn_id='data_fs')     # Make sure this airflow connection exists
data_dir = data_fs.get_path()           # get its root path
file_path = os.path.join(data_dir, FILENAME)


@task
def getVotes():
   """"""
  data_fs = FSHook(conn_id='data_fs')     # Make sure this airflow connection exists
  data_dir = data_fs.get_path()           # get its root path
  file_path = os.path.join(data_dir, FILENAME)
  
  return to_return # Passed in decorator function: t2 = func(t1)


@task
def <func2>(<returned>): # in new syntax, callables can take regular arguments, not op_kwargs/op_args
# Here, we have the parameter set to receive an XCom key called the 'return_value'
   """"""
   print(f"got XCom return value: {<returned>}")


@dag(
   schedule_interval="@once",
   start_date=datetime.utcnow(),
   catchup=False,
   default_view='graph',
   is_paused_upon_creation=True,
   tags=['', ''],
)
def <name_of_dag>():  # dag name derives from decorator function name; can also take parameter    
   """"""
   t1 = <func1>()  # task names derive from function names; modifies if called more than once
   t2 = <func2>(t1)


   t1 >> t2


dag = <name_of_dag>()


