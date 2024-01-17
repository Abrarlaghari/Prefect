import duckdb
import pandas as pd
import requests
from datetime import datetime
from prefect import flow, task


@task
def time():
    return datetime.utcnow().isoformat()


@flow
def testFlow2():
    info = time()
    print(info)
