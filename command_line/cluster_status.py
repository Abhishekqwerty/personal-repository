# Python Script for checking the status of cloudera services
import sys
from credentials import Credentials

credentials1 = sys.argv
hostname = credentials1[2]
portNumber = credentials1[4]
username = credentials1[6]
password = credentials1[8]
version = credentials1[10]
cluster = credentials1[12]

x=Credentials(hostname,portNumber,username,password,version,cluster)
for keys in x.dictionary:
    print("===================================================")
    print("Located Service: " + (x.dictionary[keys]).name)
    print("State:  "+x.dictionary[keys].serviceState + "\n" + "Health:  "+x.dictionary[keys].healthSummary)
