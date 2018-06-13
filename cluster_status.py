import sys
from cm_api.api_client import ApiResource


def status(host, user, passw):
    cm_host = str(hostname)
    api = ApiResource(cm_host, 7180, username=str(username), password=str(password), version=9)

    # Get a list of all clusters
    cluster = api.get_cluster("Cloudera QuickStart")
    service_list = cluster.get_all_services()
    for service in service_list:
        if service.type == "OOZIE":
            print(
            "===================================================")
            print("Entered Oozie")
            oozie_service = service;
            print
            ("Located Oozie Service: " + service.name)
            print("State:  "+oozie_service.serviceState + "\n" + "Health:  "+oozie_service.healthSummary)

        if service.type == "KS_INDEXER":
            print
            ("===================================================")
            print("Entered ks_indexer")
            ks_indexer_service = service;
            print
            ("Located ks_indexer Service: " + service.name)
            print("State:  "+ks_indexer_service.serviceState + "\n" + "Health:  "+ks_indexer_service.healthSummary)

        if service.type == "SQOOP":
            print
            ("===================================================")
            print("Entered sqoop")
            sqoop_service = service;
            print
            ("Located sqoop Service: " + service.name)
            print("State:  "+sqoop_service.serviceState + "\n" + "Health:  "+sqoop_service.healthSummary)

        if service.type == "ZOOKEEPER":
            print
            ("===================================================")
            print("Entered zookeeper")
            zookeeper_service = service;
            print
            ("Located zookeeper Service: " + service.name)
            print("State:  "+zookeeper_service.serviceState + "\n" + "Health:  "+zookeeper_service.healthSummary)

        if service.type == "HUE":
            print
            ("===================================================")
            print("Entered hue")
            hue_service = service;
            print
            ("Located hue Service: " + service.name)
            print("State:  "+hue_service.serviceState + "\n" + "Health:  "+hue_service.healthSummary)

        if service.type == "FLUME":
            print
            ("===================================================")
            print("Entered flume")
            flume_service = service;
            print
            ("Located flume Service: " + service.name)
            print("State:  "+flume_service.serviceState + "\n" + "Health:  "+flume_service.healthSummary)

        if service.type == "IMPALA":
            print
            ("===================================================")
            print("Entered impala")
            impala_service = service;
            print
            ("Located impala Service: " + service.name)
            print("State:  "+impala_service.serviceState + "\n" + "Health:  "+impala_service.healthSummary)

        if service.type == "HDFS":
            print
            ("===================================================")
            print("Entered hdfs")
            hdfs_service = service;
            print
            ("Located hdfs Service: " + service.name)
            print("State:  "+hdfs_service.serviceState + "\n" + "Health:  "+hdfs_service.healthSummary)

        if service.type == "SOLR":
            print
            ("===================================================")
            print("Entered solr")
            solr_service = service;
            print
            ("Located solr Service: " + service.name)
            print("State:  "+solr_service.serviceState + "\n" + "Health:  "+solr_service.healthSummary)

        if service.type == "HBASE":
            print
            ("===================================================")
            print("Entered hbase")
            hbase_service = service;
            print
            ("Located hbase Service: " + service.name)
            print("State:  "+hbase_service.serviceState + "\n" + "Health:  "+hbase_service.healthSummary)

        if service.type == "YARN":
            print
            ("===================================================")
            print("Entered yarn")
            yarn_service = service;
            print
            ("Located yarn Service: " + service.name)
            print("State:  "+yarn_service.serviceState + "\n" + "Health:  "+yarn_service.healthSummary)

        if service.type == "HIVE":
            print
            ("===================================================")
            print("Entered hive")
            hive_service = service;
            print
            ("Located hive Service: " + service.name)
            print("State:  "+hive_service.serviceState + "\n" + "Health:  "+hive_service.healthSummary)

        if service.type == "SPARK":
            print
            ("===================================================")
            print("Entered spark")
            spark_service = service;
            print
            ("Located spark Service: " + service.name)
            print("State:  "+spark_service.serviceState + "\n" + "Health:  "+spark_service.healthSummary)

        if service.type == "SENTRY":
            print
            ("===================================================")
            print("Entered sentry")
            sentry_service = service;
            print
            ("Located sentry Service: " + service.name)
            print("State:  "+sentry_service.serviceState + "\n" + "Health:  "+sentry_service.healthSummary)


credentials = sys.argv
hostname = credentials[2]
username = credentials[4]
password = credentials[6]
status(hostname, username, password)
