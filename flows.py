from datetime import datetime
import httpx
from prefect import flow, task
import numpy as np
from time import sleep
import random
from prefect.tasks import task_input_hash
from datetime import timedelta
base_url = "https://api.open-meteo.com/v1"

@flow(log_prints=True)
def meteo_flow(lon: float = 0, lat: float = 0, dt: datetime = None):
    dt = dt if dt else datetime.now()
    temp =  get_temperature(lon, lat)
    print(temp)
    temp_kelvin = c_to_k(temp)
    print(temp_kelvin)

@flow()
def big_flow():
    meteo_flow()
    recite_illiad()


@task(retries=4, retry_delay_seconds=5, cache_expiration=timedelta(seconds=1000), cache_key_fn=task_input_hash)
def get_temperature(lon: float = 0, lat: float = 0, dt: datetime = None) -> np.array:
    dt = dt if dt else datetime.now()
    import random
    failthreshold = 0.4
    if random.random() > failthreshold:
        raise ValueError("Bam")
    params={"latitude": lat,
            "longitude": lon,
            "hourly": "temperature_2m"}
    print(params)
    temp = np.array(httpx.get(f"{base_url}/forecast", params=params).json()["hourly"]["temperature_2m"], dtype=float)
    return temp

@task
def c_to_k(temp: np.array = np.array([])):
    return temp + 273.15

@task
def recite_illiad():
    with open("ilias.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            sleep(1)
    return
