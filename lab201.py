from datetime import datetime
from flows import big_flow, meteo_flow

from prefect.deployments import Deployment
from prefect.filesystems import Azure
from prefect.server.schemas.schedules import CronSchedule

az_block = Azure.load("azure-block-prefect-training")

cr = CronSchedule(cron="0 0 * * *", timezone="Europe/Brussels")
deploy = Deployment.build_from_flow(
    flow=meteo_flow,
    name="deployment_azure",
    storage=az_block
)

if __name__ == "__main__":
    deploy.apply()