import pymongo

client = pymongo.MongoClient("mongodb://xrodneylee:xrodneylee@" \
                                       + "cluster0-shard-00-00-5ekni.mongodb.net:27017," \
                                       + "cluster0-shard-00-01-5ekni.mongodb.net:27017," \
                                       + "cluster0-shard-00-02-5ekni.mongodb.net:27017/admin?" \
                                       + "ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client['azure-billing']