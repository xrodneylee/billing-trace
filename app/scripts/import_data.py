from ..services.azure import AzureCredential, AzureRatecard, AzureUsage
import json
from ..common.util import AzureUtil
from config import tenant_collection, subscription_collection, subscription_group_collection,\
                   azure_ratecard_collection
# import configparser
# import requests
def job():
    data = []

    tenants = json.loads(AzureUtil.get_all_tenant())
    for tenant in tenants:
        tenant['subscriptions'] = list()
        subscriptions = json.loads(AzureUtil.get_all_subscription_by_tenant(tenant['tenant']))
        for subscription in subscriptions:
            tenant['subscriptions'].append({
                "subscription": subscription['subscriptionId'],
                "offer_durable_id": subscription['offer_durable_id']
            })

            credential = AzureCredential(tenant['tenant'], tenant['client_id'], tenant['client_secret'])
            ratecard = AzureRatecard(credential.invoke().json()['access_token'],
                                     subscription['subscriptionId'],
                                     subscription['offer_durable_id'])
            data.append(tenant)
            for document in ratecard.invoke().json()['Meters']:
                if azure_ratecard_collection.find_one({"MeterId": document['MeterId']}):
                    pass
                else:
                    azure_ratecard_collection.insert(document, check_keys=False)
            print("@@@@@@@@@@@@@@@@@@@")

    # print(data)
# config = configparser.ConfigParser()
# config.read_file(open("secret.properties"))

# tenant = config.get("Azure", "tenant")
# client_id = config.get("Azure", "client_id")
# client_secret = config.get("Azure", "client_secret")
# subscription = config.get("Azure", "subscription")
# offer_durable_id = config.get("Azure", "offer_durable_id")

# def get_ratecard():
    # credential = AzureCredential(tenant, client_id, client_secret)
    # ratecard = AzureRatecard(credential.invoke().json()['access_token'],
    #                          subscription,
    #                          offer_durable_id)
#     # for document in ratecard.invoke().json()['Meters']:
    # azure_ratecard_collection.remove({})
    # azure_ratecard_collection.insert(ratecard.invoke().json()['Meters'], check_keys=False)
#     # print(ratecard.invoke().json())


    