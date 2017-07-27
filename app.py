# Copyright (c) 2017, Lee Guan Pu
# All rights reserved.

import pymongo
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient("mongodb://xrodneylee:xrodneylee@ \
                                        cluster0-shard-00-00-5ekni.mongodb.net:27017, \
                                        cluster0-shard-00-01-5ekni.mongodb.net:27017, \
                                        cluster0-shard-00-02-5ekni.mongodb.net:27017/admin? \
                                        ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client['azure-billing']
collectionOfUsage = db.usage
collectionOfRatecard = db.ratecard


if __name__ == '__main__':
    app.run(debug=True)