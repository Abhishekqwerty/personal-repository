import sys
from cm_api.api_client import ApiResource

def start(host, user, passw):
	cm_host = str(host)
	api = ApiResource(cm_host, 7180, username=str(username) , password=str(password), version=9)
	mgmt = api.get_cloudera_manager().get_service()
	mgmt.restart()
	print("Services successfully started")


credentials = sys.argv
hostname = credentials[2]
username = credentials[4]
password = credentials[6]
print(hostname + " " + username + " " + password)
start(hostname, username, password)
