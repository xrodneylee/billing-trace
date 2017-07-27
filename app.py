# Copyright (c) 2017, Lee Guan Pu
# All rights reserved.

from flask import Flask
from flask_restful import Api
import pymongo

app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient("mongodb://xrodneylee:xrodneylee@cluster0-shard-00-00-5ekni.mongodb.net:27017,cluster0-shard-00-01-5ekni.mongodb.net:27017,cluster0-shard-00-02-5ekni.mongodb.net:27017/admin?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client.lab
collection = db.test_collection


# for i in range(20):
#     post = {"author": "Mike", \
#     "text": "My first blog post!",\
#     "tags": ["mongodb", "python", "pymongo"],\
#     "date": datetime.datetime.utcnow(), \
#     "aa": i}
#     post_id = collection.insert_one(post).inserted_id
#     print(post_id)
if __name__ == '__main__':
    app.run(debug=True)