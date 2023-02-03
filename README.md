# _airflow-review_

#### By _**Alejandro Socarras**_

#### _Unit 3, Chapter 12 Code Review_

## Description

Practicing XCOMs and file sensors in Airflow 

## Assignment Instructions: 

Write a DAG meeting the following criteria:

- Use a file sensor to check whether the votes.csv file has been uploaded to the data/ folder of this repository.

- Have a task that reads each row in votes.csv, and checks whether that value is in the flavors_choices list defined above. If it is, append it to a new list called valid_votes. This task should return the valid_votes list.

- In another task, use a Python function that takes a list as an argument, and prints the item that appear the most times in that list.

- Pass the return_value XCom from the first task as an argument to the second task.

- Use decorators to define the tasks.

## Setup/Installation Requirements

_Clone repo to your local system:_

1. Make a directory on your disk where you would like to clone the repo.

2. Copy the repo link: https://github.com/apsocarras/airflow-review2.git (available if you click the green "Code" dropdown button on this page).

3. Open your terminal and change into the directory you made (`cd /path/to/new/directory`).

4. Type `git clone ` and paste the URL.

_Install required packages:_

The only package you should need to install in addition to base python libraries (v3.7) is **Airflow** (v2.3.2). Two other pieces of software are required: [Docker](https://www.docker.com/products/docker-desktop/) and [gcloud CLI](https://cloud.google.com/sdk/docs/install). Follow the linked instructions and install these for your operating system before running the following commands in your new project directory: 

```bash 
# Create and activate virtual environment
virtualenv -p python3.7 venv 
source venv/bin/activate

# Install Airflow with pip
AIRFLOW_VERSION=2.3.2 
PYTHON_VERSION=3.7 
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[async,postgres,google]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Go to airflow subdirectory
cd airflow 
mkdir ./plugins ./logs # create subdirectories 

# Set the .env  
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```
_Start and run Airflow_
We're now ready to test our file-sensing DAG (`cake.py`) in an Airflow Docker container. First start Docker by opening Docker Desktop (or [via CLI](https://docs.docker.com/config/daemon/start/)), then run the following:
```bash 
# Initialize Airflow
docker compose up airflow-init
# Start Docker Container 
docker compose up 
# Create a file connection
./airflow.sh connections add --conn-type=fs --conn-extra='{"path": "/opt/airflow/data"}' data_fs
# Start the dag
./airflow.sh dags test cake.py 
# Download data into the data directory
cd ./data
gsutil -m cp gs://data.datastack.academy/airflow_cr_2/votes.csv .
```
After a few moments, the DAG's file sensor should detect the added file and run the rest of the tasks.

_Note_: The `airflow.sh` script comes from Apache directly, but `docker-compose` with `docker compose` (i.e. remove the `-`). This `-` is included in the script even the latest version of Airflow, even though the `docker compose` command is run without it.

## Known Bugs

_No known bugs._

## License

_[MIT License](https://opensource.org/licenses/MIT)_

Copyright (c) _2.3.23_ Alejandro Socarras

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


