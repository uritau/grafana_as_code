# Grafana as Code

## Requirements

* Python 3
> `mkvirtualenv grafana`
* Install requirements:
> `pip install -r requirements.txt`
* Running grafana or start one with:
> `docker-compose up -d`

## First steps

1) Create dashboard code in python, like `./example.dashboard.py`
2) Export Python generated code to json
> `generate-dashboard -o example.json example.dashboard.py`
3) Load JSON in grafana
> `python grafana_push.py example.json`

## Configuration
* You can provide a configuration file setting the environment variable "`GAC_CONFIG`" with the path of a file with the configuration, in `.ini` format.
* Configuration file:
```ini
[grafana]
host = GRAFANA_URL
user = ADMIN_USER
password = ADMIN_USER_PASSWORD
port = GRAFANA_PORT
protocol = GRAFANA_PROTOCOL
```

## Based on
[grafanalib](https://github.com/weaveworks/grafanalib) - Generate JSON Dashboards from python

[grafana_api](https://github.com/m0nhawk/grafana_api) - Upload Dashboards to Grafana

## To Do
 * Get rid of spaghetty code.
 * Add testing.
 * Add github actions to pylint and test.
 * Add the possibility to define data origins from a .yaml config file.
 * Add the possibility to configure user groups and permissions.
 * Add meta modules to create (with .yaml configuration) standard config parts (RDS, EC2, etc).