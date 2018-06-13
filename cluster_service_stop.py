import sys
from cm_api.api_client import ApiResource

def stop(host, user, passw):
	cm_host = str(host)
	api = ApiResource(cm_host, 7180, username=str(username) , password=str(password), version=9)
	mgmt = api.get_cloudera_manager().get_service()
	mgmt.stop()
	print("Services stopped")


credentials = sys.argv
hostname = credentials[2]
username = credentials[4]
password = credentials[6]
stop(hostname, username, password)
