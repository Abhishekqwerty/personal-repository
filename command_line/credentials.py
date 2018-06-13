# Python Script for connecting to cloudera with it's credentials
from cm_api.api_client import ApiResource

class Credentials:

    def __init__(self,host,port,user,passw,version,cluster):
        self.api = ApiResource(str(host), port, username=str(user) , password=str(passw), version=int(version))
        cluster1 = self.api.get_cluster(cluster)
        self.service_list = cluster1.get_all_services()
        self.serviceList=["OOZIE","KS_INDEXER","SQOOP","ZOOKEEPER","HUE","FLUME","IMPALA","HDFS","SOLR","HBASE","YARN","HIVE","SPARK","SENTRY"]
        self.list=[]


        for service in self.service_list:
            if service.type in self.serviceList:
                self.list.append(service)

        self.dictionary = dict(zip(self.serviceList,self.list))

