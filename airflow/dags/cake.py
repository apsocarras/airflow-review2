from datetime import datetime
from airflow import DAG
from airflow.decorators import dag, task


@task
def <func1>():
   """"""
  return <to_return> # Passed in decorator function: t2 = func(t1)


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


