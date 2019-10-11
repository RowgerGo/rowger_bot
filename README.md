"# rowger_bot" 

```shell script
docker run --name=coolq -d -p 8060:9000 -p8099:8099  -v    /home/workplace/pyProject/coolq-data:/home/user/coolq -e VNC_PASSWD=12345678 -e COOLQ_ACCOUNT=2976939147  coolq/wine-coolq
```