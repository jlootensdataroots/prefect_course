from datetime import datetime
from prefect import flow
from flows import big_flow, meteo_flow

from prefect.deployments import Deployment
from prefect.filesystems import Azure
from prefect.server.schemas.schedules import CronSchedule

az_block = Azure.load("azure-block-prefect-training")

@flow()
def upload_to_azure() -> None:
    az_block.put_directory(local_path="images", to_path="upload_to_azure/images")
    
deploy = Deployment.build_from_flow(
    flow=upload_to_azure,
    name="deployment_upload_azure",
)

if __name__ == "__main__":
    deploy.apply()