import sys
from cm_api.api_client import ApiResource

def operations(host, user, passw):
	cm_host = str(host)
	global api
	api = ApiResource(cm_host, 7180, username=str(username) , password=str(password), version=9)
	print("Connected to Cloudera")
	global cluster
	cluster = api.get_cluster("Cloudera QuickStart")
	global service_list
	service_list = cluster.get_all_services()
	

	for service in service_list:
		if service.type == "OOZIE":
			global oozie_service
			oozie_service = service;
		
		if service.type == "KS_INDEXER":
			global ks_indexer_service
			ks_indexer_service = service;

		if service.type == "SQOOP":
			global sqoop_service
			sqoop_service = service;

		if service.type == "ZOOKEEPER":
			global zookeeper_service
			zookeeper_service = service;

		if service.type == "HUE":
			global hue_service
			hue_service = service;

		if service.type == "FLUME":
			global flume_service
			flume_service = service;

		if service.type == "IMPALA":
			global impala_service
			impala_service = service;

		if service.type == "HDFS":
			global hdfs_service
			hdfs_service = service;

		if service.type == "SOLR":
			global solr_service
			solr_service = service;

		if service.type == "HBASE":
			global hbase_service
			hbase_service = service;

		if service.type == "YARN":
			global yarn_service
			yarn_service = service;

		if service.type == "HIVE":
			global hive_service
			hive_service = service;
		
		if service.type == "SPARK":
			global spark_service
			spark_service = service;
		
		if service.type == "SENTRY":
			global sentry_service
			sentry_service = service;
	
	while(True):
		choice = input("\n1.  Status \n2.  Start \n3.  Stop\n4.  Quit\n")
		switch={"1":status, "2":start, "3":stop}
	
		if choice == 1:
			switch["1"]()
		elif choice == 2:
			switch["2"]()
		elif choice == 3:
			switch["3"]()
		elif choice == 4:
			break


def status():
			print("===================================================")
			print("Entered Oozie")
			print("Located Oozie Service: " + oozie_service.name)
			print("State:  "+ oozie_service.serviceState + "\n" + "Health:  "+ oozie_service.healthSummary)


			print("===================================================")
			print("Entered ks_indexer")
			print("Located ks_indexer Service: " + ks_indexer_service.name)
			print("State:  "+ks_indexer_service.serviceState + "\n" + "Health:  "+ks_indexer_service.healthSummary)

		
			print("===================================================")
			print("Entered sqoop")
			print("Located sqoop Service: " + sqoop_service.name)
			print("State:  "+sqoop_service.serviceState + "\n" + "Health:  "+sqoop_service.healthSummary)
		

		
			print("===================================================")
			print("Entered zookeeper")
			print("Located zookeeper Service: " + zookeeper_service.name)
			print("State:  "+zookeeper_service.serviceState + "\n" + "Health:  "+zookeeper_service.healthSummary)
		

		
			print("===================================================")
			print("Entered hue")
			print("Located hue Service: " + hue_service.name)
			print("State:  "+hue_service.serviceState + "\n" + "Health:  "+hue_service.healthSummary)
		

		
			print("===================================================")
			print("Entered flume")
			print("Located flume Service: " + flume_service.name)
			print("State:  "+flume_service.serviceState + "\n" + "Health:  "+flume_service.healthSummary)
		

		
			print("===================================================")
			print("Entered impala")
			print("Located impala Service: " + impala_service.name)
			print("State:  "+impala_service.serviceState + "\n" + "Health:  "+impala_service.healthSummary)
		

		
			print("===================================================")
			print("Entered hdfs")
			print("Located hdfs Service: " + hdfs_service.name)
			print("State:  "+hdfs_service.serviceState + "\n" + "Health:  "+hdfs_service.healthSummary)
		

		
			print("===================================================")
			print("Entered solr")
			print("Located solr Service: " + solr_service.name)
			print("State:  "+solr_service.serviceState + "\n" + "Health:  "+solr_service.healthSummary)
		

		
			print("===================================================")
			print("Entered hbase")
			print("Located hbase Service: " + hbase_service.name)
			print("State:  "+hbase_service.serviceState + "\n" + "Health:  "+hbase_service.healthSummary)
		

		
			print("===================================================")
			print("Entered yarn")
			print("Located yarn Service: " + yarn_service.name)
			print("State:  "+yarn_service.serviceState + "\n" + "Health:  "+yarn_service.healthSummary)


		
			print("===================================================")
			print("Entered hive")
			print("Located hive Service: " + hive_service.name)
			print("State:  "+hive_service.serviceState + "\n" + "Health:  "+hive_service.healthSummary)

		
			print("===================================================")
			print("Entered spark")
			print("Located spark Service: " + spark_service.name)
			print("State:  "+spark_service.serviceState + "\n" + "Health:  "+spark_service.healthSummary)

	
			print("===================================================")
			print("Entered sentry")
			print("Located sentry Service: " + sentry_service.name)
			print("State:  "+sentry_service.serviceState + "\n" + "Health:  "+sentry_service.healthSummary)

def start():
	print("\nEnter your choice\n")
	start = input("1.  Start/Restart all services\n2.  Start specific service\n")   
	if start == 1:
		mgmt = api.get_cloudera_manager().get_service()
		mgmt.restart()
	elif start == 2:
		name = raw_input("\nEnter the name of service as in cloudera\n")		#use input() for python3 interpreter
		if name.lower().strip() == "oozie":
			oozie_service.restart()
		elif name.lower().strip() == "ks_indexer":
			ks_indexer_service.restart()
		elif name.lower().strip() == "sqoop":
			sqoop_service.restart()
		elif name.lower().strip() == "zookeeper":
			zookeeper_service.restart()
		elif name.lower().strip() == "hue":
			hue_service.restart()
		elif name.lower().strip() == "flume":
			flume_service.restart()
		elif name.lower().strip() == "impala":
			impala_service.restart()
		elif name.lower().strip() == "hdfs":
			hdfs_service.restart()
		elif name.lower().strip() == "solr":
			solr_service.restart()
		elif name.lower().strip() == "hbase":
			hbase_service.restart()
		elif name.lower().strip() == "yarn":
			yarn_service.restart()
		elif name.lower().strip() == "hive":
			hive_service.restart()
		elif name.lower().strip() == "spark":
			spark_service.restart()
		elif name.lower().strip() == "sentry":
			sentry_service.restart()
		else:
			print("Name of service is not correct")


def stop():
	print("\nEnter your choice")
	stop = input("\n1.  Stop all services\n2.  Stop specific service\n")	
	if stop == 1:
		mgmt = api.get_cloudera_manager().get_service()
		mgmt.stop()
	elif stop == 2:
		name = raw_input("\nEnter the name of service as in cloudera\n")	#use input() for python3 interpreter
		if name.lower().strip() == "oozie":
			oozie_service.stop()
		elif name.lower().strip() == "ks_indexer":
			ks_indexer_service.stop()
		elif name.lower().strip() == "sqoop":
			sqoop_service.stop()
		elif name.lower().strip() == "zookeeper":
			zookeeper_service.stop()
		elif name.lower().strip() == "hue":
			hue_service.stop()
		elif name.lower().strip() == "flume":
			flume_service.stop()
		elif name.lower().strip() == "impala":
			impala_service.stop()
		elif name.lower().strip() == "hdfs":
			hdfs_service.stop()
		elif name.lower().strip() == "solr":
			solr_service.stop()
		elif name.lower().strip() == "hbase":
			hbase_service.stop()
		elif name.lower().strip() == "yarn":
			yarn_service.stop()
		elif name.lower().strip() == "hive":
			hive_service.stop()
		elif name.lower().strip() == "spark":
			spark_service.stop()
		elif name.lower().strip() == "sentry":
			sentry_service.stop()
		else:
			print("Name of service is not correct")


credentials = sys.argv
hostname = credentials[2]
username = credentials[4]
password = credentials[6]
operations(hostname, username, password)
