## LAB105
![lab 105, with cron schedule](images/lab105.png)
deployment created from python file with cron schedule
![lab 105, with manual schedule](images/lab105man.png)
same deployment but with manual interval schedule of 1 day, added via UI
## LAB 201
![lab 201](images/lab201.png)
result of azure deployment
## LAB 202
```
prefect deployment build flows.py:meteo_flow -n deployment-docker -ib docker-container/docker-block-prefect-training
prefect deployment apply meteo_flow-deployment.yaml 
```
![lab 202](images/lab202.png)
deployment of meteo_flow on docker block  
## LAB 203
3h05
