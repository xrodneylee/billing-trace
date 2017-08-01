""" azure settings """
from flask_restful import Resource, reqparse
from config import db
from bson.json_util import dumps
from ..services.azure import AzureCredential, AzureSubscription

parser = reqparse.RequestParser(trim=True)
parser.add_argument('tenant', required=True, type=str, help='tenant cannot be blank')
parser.add_argument('client_id', required=True, type=str, help='client_id cannot be blank')
parser.add_argument('client_secret', required=True, type=str, help='client_secret cannot be blank')

tenant_collection = db['tenant']
subscription_collection = db['subscription']

class Tenant(Resource):
    """
    Tenant restful api
    """
    def get(self, tenant=None):
        """get single/all tenant
        """
        if tenant:
            return dumps(tenant_collection.find_one({"tenant": tenant}, {"_id": 0}))
        else:
            return dumps(tenant_collection.find({}, {"_id": 0}))

    def post(self):
        """create new tenant
        """
        args = parser.parse_args()

        if tenant_collection.find_one({"tenant": args['tenant']}):
            return {"response": "tenant already exists."}
        else:
            tenant_collection.insert_one({'tenant': args['tenant'],
                                          'client_id': args['client_id'],
                                          'client_secret': args['client_secret']})
            return dumps(tenant_collection.find_one({"tenant": args['tenant']}, {"_id": 0}))

    def delete(self, tenant=None):
        """delete tenant
        """
        if tenant:
            tenant_collection.delete_one({"tenant": tenant})
        else:
            return {"response": "tenant doesn't exist."}

    def put(self):
        """update tenant
        """
        args = parser.parse_args()

        if tenant_collection.find_one({"tenant": args['tenant']}):
            tenant_collection.update_one({"tenant": args['tenant']},
                                         {"$set" : {
                                             'client_id': args['client_id'],
                                             'client_secret': args['client_secret']
                                             }
                                         })
            return dumps(tenant_collection.find_one({"tenant": args['tenant']}, {"_id": 0}))
        else:
            return {"response": "tenant doesn't exist."}


class Subscription(Resource):
    
    def get(self, subscription=None):
        if subscription:
            return dumps(subscription_collection.find_one({"subscriptionId": subscription}, {"subscriptionId": 1, "displayName": 1, "_id": 0}))
        else:
            return dumps(subscription_collection.find({}, {"subscriptionId": 1, "displayName": 1,"_id": 0}))

    def post(self):
        args = parser.parse_args()

        credential = AzureCredential(args['tenant'], args['client_id'], args['client_secret'])
        token = credential.invoke().json()['access_token']
        subscriptions = AzureSubscription(args['tenant'], token)
        for document in subscriptions.invoke().json()['value']:
            if subscription_collection.find_one({"subscriptionId": document['subscriptionId']}):
                pass
            else:
                subscription_collection.insert_one(document)
        return dumps(subscription_collection.find({}, {"subscriptionId": 1, "displayName": 1, "_id": 0}))

    def delete(self, subscription=None):
        if subscription:
            subscription_collection.delete_one({"subscriptionId": subscription})
        else:
            return {"response": "subscriptionId doesn't exist."}

    def put(self):
        pass
