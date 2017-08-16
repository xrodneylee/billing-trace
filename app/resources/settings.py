""" azure settings """
from flask_restful import Resource, reqparse
from config import tenant_collection, subscription_collection, subscription_group_collection
from bson.json_util import dumps
from ..services.azure import AzureCredential, AzureSubscription

parser = reqparse.RequestParser(trim=True)
parser.add_argument('tenant', required=True, type=str, help='tenant cannot be blank')
parser.add_argument('client_id', required=True, type=str, help='client_id cannot be blank')
parser.add_argument('client_secret', required=True, type=str, help='client_secret cannot be blank')

subscription_parser = reqparse.RequestParser(trim=True)
subscription_parser.add_argument('subscription', required=True, type=str, help='subscription cannot be blank')
subscription_parser.add_argument('offer_durable_id', required=False, type=str)

group_parser = reqparse.RequestParser(trim=True)
group_parser.add_argument('groupName', required=True, type=str, help='groupName cannot be blank')
group_parser.add_argument('subscriptions', required=True, type=str, help='subscriptions cannot be blank', action='append')



class Tenant(Resource):
    """Tenant restful api
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
    """Subscription restful api
    """
    def get(self, subscription=None):
        if subscription:
            return dumps(subscription_collection.find_one({"subscriptionId": subscription},
                                                          {"subscriptionId": 1,
                                                           "displayName": 1,
                                                           "_id": 0}))
        else:
            return dumps(subscription_collection.find({}, {"subscriptionId": 1,
                                                           "displayName": 1,
                                                           "_id": 0}))

    def post(self):
        """sync subscriptsions of tenant to mongodb
        """
        # TODO: duplicate data
        args = parser.parse_args()

        credential = AzureCredential(args['tenant'], args['client_id'], args['client_secret'])
        token = credential.invoke().json()['access_token']
        subscriptions = AzureSubscription(args['tenant'], token)
        for document in subscriptions.invoke().json()['value']:
            if subscription_collection.find_one({"subscriptionId": document['subscriptionId']}):
                pass
            else:
                document['tenant'] = args['tenant']
                subscription_collection.insert_one(document)
        return dumps(subscription_collection.find({"tenant": args['tenant']},
                                                  {"subscriptionId": 1,
                                                   "displayName": 1,
                                                   "_id": 0}))

    def delete(self, subscription=None):
        if subscription:
            subscription_collection.delete_one({"subscriptionId": subscription})
        else:
            return {"response": "subscriptionId doesn't exist."}

    def put(self):
        args = subscription_parser.parse_args()

        if subscription_collection.find_one({"subscriptionId": args['subscription']}):
            subscription_collection.update_one({"subscriptionId": args['subscription']},
                                               {"$set" : {
                                                   'offer_durable_id': args['offer_durable_id']
                                                   }
                                               })
            return dumps(subscription_collection.find_one({"subscriptionId": args['subscription']}, {"_id": 0}))
        else:
            return {"response": "subscriptionId doesn't exist."}


class Group(Resource):
    """Subscription group
    """
    def get(self, group_name=None):
        if group_name:
            return dumps(subscription_group_collection.find_one({"groupName": group_name},
                                                                {"groupName": 1,
                                                                 "subscriptions": 1,
                                                                 "_id": 0}))
        else:
            return dumps(subscription_group_collection.find({}, {"groupName": 1,
                                                                 "subscriptions": 1,
                                                                 "_id": 0}))

    def post(self):
        args = group_parser.parse_args()

        if subscription_group_collection.find_one({"groupName": args['groupName']}):
            return {"response": "groupName already exists."}
        else:
            subscription_group_collection.insert_one(args)
            return dumps(subscription_group_collection.find_one({"groupName": args['groupName']},
                                                                {"_id": 0}))

    def delete(self):
        pass

    def put(self):
        pass
