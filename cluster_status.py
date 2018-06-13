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
            print(oozie_service.serviceState + "\n" + oozie_service.healthSummary)

        if service.type == "KS_INDEXER":
            print
            ("===================================================")
            print("Entered ks_indexer")
            ks_indexer_service = service;
            print
            ("Located ks_indexer Service: " + service.name)
            print(ks_indexer_service.serviceState + "\n" + ks_indexer_service.healthSummary)

        if service.type == "SQOOP":
            print
            ("===================================================")
            print("Entered sqoop")
            sqoop_service = service;
            print
            ("Located sqoop Service: " + service.name)
            print(sqoop_service.serviceState + "\n" + sqoop_service.healthSummary)

        if service.type == "ZOOKEEPER":
            print
            ("===================================================")
            print("Entered zookeeper")
            zookeeper_service = service;
            print
            ("Located zookeeper Service: " + service.name)
            print(zookeeper_service.serviceState + "\n" + zookeeper_service.healthSummary)

        if service.type == "HUE":
            print
            ("===================================================")
            print("Entered hue")
            hue_service = service;
            print
            ("Located hue Service: " + service.name)
            print(hue_service.serviceState + "\n" + hue_service.healthSummary)

        if service.type == "FLUME":
            print
            ("===================================================")
            print("Entered flume")
            flume_service = service;
            print
            ("Located flume Service: " + service.name)
            print(flume_service.serviceState + "\n" + flume_service.healthSummary)

        if service.type == "IMPALA":
            print
            ("===================================================")
            print("Entered impala")
            impala_service = service;
            print
            ("Located impala Service: " + service.name)
            print(impala_service.serviceState + "\n" + impala_service.healthSummary)

        if service.type == "HDFS":
            print
            ("===================================================")
            print("Entered hdfs")
            hdfs_service = service;
            print
            ("Located hdfs Service: " + service.name)
            print(hdfs_service.serviceState + "\n" + hdfs_service.healthSummary)

        if service.type == "SOLR":
            print
            ("===================================================")
            print("Entered solr")
            solr_service = service;
            print
            ("Located solr Service: " + service.name)
            print(solr_service.serviceState + "\n" + solr_service.healthSummary)

        if service.type == "HBASE":
            print
            ("===================================================")
            print("Entered hbase")
            hbase_service = service;
            print
            ("Located hbase Service: " + service.name)
            print(hbase_service.serviceState + "\n" + hbase_service.healthSummary)

        if service.type == "YARN":
            print
            ("===================================================")
            print("Entered yarn")
            yarn_service = service;
            print
            ("Located yarn Service: " + service.name)
            print(yarn_service.serviceState + "\n" + yarn_service.healthSummary)

        if service.type == "HIVE":
            print
            ("===================================================")
            print("Entered hive")
            hive_service = service;
            print
            ("Located hive Service: " + service.name)
            print(hive_service.serviceState + "\n" + hive_service.healthSummary)

        if service.type == "SPARK":
            print
            ("===================================================")
            print("Entered spark")
            spark_service = service;
            print
            ("Located spark Service: " + service.name)
            print(spark_service.serviceState + "\n" + spark_service.healthSummary)

        if service.type == "SENTRY":
            print
            ("===================================================")
            print("Entered sentry")
            sentry_service = service;
            print
            ("Located sentry Service: " + service.name)
            print(sentry_service.serviceState + "\n" + sentry_service.healthSummary)


credentials = sys.argv
hostname = credentials[2]
username = credentials[4]
password = credentials[6]
status(hostname, username, password)
