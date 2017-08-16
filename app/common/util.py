from config import tenant_collection, subscription_collection,\
                   subscription_group_collection, azure_ratecard_collection
from bson.json_util import dumps

class AzureUtil():
    
    @staticmethod
    def get_all_tenant():
        return dumps(tenant_collection.find({}, {"_id": 0}))

    @staticmethod
    def get_all_subscription_by_tenant(tenant):
        return dumps(subscription_collection.find({"tenant": tenant}, {"subscriptionId": 1,
                                                                       "offer_durable_id": 1,
                                                                       "_id": 0}))
