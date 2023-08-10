Python API to get the server usage. CPU, SWAP and Memory percent, usage in GB, free space, etc

## Setup

Before running the project we need to install the requirements, in console write `pip install -r requirements.txt`

## Run the project

### Windows

`py main.py`

### Linux & Mac

`python3 main.py`

## To create systemctl service

Go to `/etc/systemd/system` and create a file `system-usage.service` and write:
```
[Unit]
Description="System Usage API"
After=network.target

[Service]
User=server
WorkingDirectory=/home/server/Scripts/system_usage/
ExecStart=/home/server/.asdf/shims/python3.10 main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

and then `sudo systemctl enable system-usage`

## Endpoints

- <b>GET</b> _/system-usage_

  #### Response:

  200

  ```json
  {
    "CPU": {
      "cores": 12,
      "percent": 2.3,
      "temperature": 61.9
    },
    "MEMORY": {
      "available": 10426122240,
      "percent": 36.6,
      "total": 16444125184,
      "used": 4657848320
    },
    "SWAP": {
      "available": 32000438272,
      "percent": 0.0,
      "total": 32000438272,
      "used": 0
    },
    "DISK": {
      "available": 121003053056,
      "percent": 43.4,
      "total": 225394515968,
      "used": 92867510272
    }
  }
  ```
