import pymongo
from flask import Flask
from flask_restful import Api
import requests
from .resources.mock import Mock
from .resources.settings import AzureConfig

app = Flask(__name__)
api = Api(app)

client = pymongo.MongoClient("mongodb://xrodneylee:xrodneylee@ \
                                        cluster0-shard-00-00-5ekni.mongodb.net:27017, \
                                        cluster0-shard-00-01-5ekni.mongodb.net:27017, \
                                        cluster0-shard-00-02-5ekni.mongodb.net:27017/admin? \
                                        ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
db = client['azure-billing']

# restful api
api.add_resource(Mock, '/mock') # , '/mock/<str:id>'

# settings
api.add_resource(AzureConfig, '/azure-config')
