from grafana_api.grafana_face import GrafanaFace
import sys
import json
import configparser
import os

# Read input parameters
json_file = sys.argv[1]

# Set configuration file
config_file = os.getenv('GAC_CONFIG', 'config.ini')

# Read configuration file
config = configparser.ConfigParser()
config.read(config_file)

grafana_host = config['grafana']['host']
grafana_user = config['grafana']['user']
grafana_password = config['grafana']['password']
grafana_port = config['grafana']['port']
grafana_protocol = config['grafana']['protocol']
#grafana_api_key = config['grafana']['api_key']

# Read json file
with open(json_file, 'r') as file:
    json_dashboard = json.loads(file.read().replace('\n', ''))

# Configure grafana conneciton
grafana_api = GrafanaFace(
#    auth=grafana_api_key, host=grafana_host
    (grafana_user, grafana_password),
    host=grafana_host,
    port=grafana_port,
    protocol=grafana_protocol
)

# Push dashboard
grafana_api.dashboard.update_dashboard(
    dashboard={'dashboard': json_dashboard, 'folderId': 0, 'overwrite': True})

# # Delete a dashboard by UID
# grafana_api.dashboard.delete_dashboard(dashboard_uid='abcdefgh')
