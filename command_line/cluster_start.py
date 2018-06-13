# Python Script for starting single or all services of cloudera
# NOTE: For starting all services the user should use "-s all" on command line
import sys
from credentials import Credentials


credentials1 = sys.argv
hostname = credentials1[2]
portNumber = credentials1[4]
username = credentials1[6]
password = credentials1[8]
version = credentials1[10]
cluster = credentials1[12]
service = credentials1[14]

x=Credentials(hostname,portNumber,username,password,version,cluster)
mgmt=x.api.get_cloudera_manager().get_service()
if service.lower().strip() == "all":
    mgmt.restart()

elif str(service).upper() in x.dictionary :
    ser=x.dictionary[str(service).upper()]
    ser.restart()

