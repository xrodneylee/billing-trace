from flask_restful import Resource, reqparse
from config import tenant_collection, subscription_collection, subscription_group_collection
from bson.json_util import dumps

class Subscriptions(Resource):
    def get(self, tenant=None):
        print(tenant)
        return dumps(subscription_collection.find({"tenant": tenant},
                                                  {"subscriptionId": 1,
                                                   "_id": 0}))
