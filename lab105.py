from datetime import datetime
from flows import big_flow, meteo_flow

from prefect.deployments import Deployment
from prefect.server.schemas.schedules import CronSchedule

cr = CronSchedule(cron="0 0 * * *", timezone="Europe/Brussels")
deploy = Deployment.build_from_flow(
    flow=meteo_flow,
    name="deployment_from_python_file",
    parameters= {"lon": 0, "lat":0, "datetime": datetime.now()},
    schedule=cr,
)

if __name__ == "__main__":
    deploy.apply()