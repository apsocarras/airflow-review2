import os 
import csv 
from datetime import datetime
from collections import Counter
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

@task
def getVotes():
  """Use file sensor to check for a file being added to the data directory; read file and return valid votes"""

  data_fs = FSHook(conn_id='data_fs')     
  data_dir = data_fs.get_path()           
  file_path = os.path.join(data_dir, FILENAME)

  with open(file_path, newline='') as csv_file: 
    vote_reader = csv.reader(csv_file)
    valid_votes = [flavor[0] for flavor in vote_reader if flavor[0] in FLAVORS]  

  return valid_votes

@task
def printWinner(valid_votes:list): 
  """Print flavor with most votes in valid_votes"""

  counter = Counter(valid_votes)
  winner = counter.most_common(1)[0]

  print(f"The winning flavor is {winner}!")

@dag(
   schedule_interval="@once",
   start_date=datetime.utcnow(),
   catchup=False,
   default_view='graph',
   is_paused_upon_creation=True,
)

def cake():      
  """"""
  wait_for_file = FileSensor(
       task_id='',
       poke_interval=15,                   # check every 15 seconds
       timeout=(30 * 60),                  # timeout after 30 minutes
       mode='poke',                        # mode: poke, reschedule
       filepath=FILENAME,                  # file path to check (relative to fs_conn)
       fs_conn_id='data_fs',               # file system connection (root path)
   )

  getVotes_task = getVotes()  
  printWinner_task = printWinner(getVotes_task)

  wait_for_file >> getVotes_task >> printWinner_task
  
dag = cake()


