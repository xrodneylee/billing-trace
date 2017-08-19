import json
from config import azure_ratecard_collection, azure_usage_collection
from ..services.azure import AzureCredential, AzureRatecard, AzureUsage
from ..common.util import AzureUtil, DatetimeUtil


def refresh_ratecard_job():
    offer_durable_id_set = set()
    azure_ratecard_collection.drop()
    tenants = json.loads(AzureUtil.get_all_tenant())

    for tenant in tenants:
        subscriptions = json.loads(AzureUtil.get_all_subscription_by_tenant(tenant['tenant']))
        credential = AzureCredential(tenant['tenant'], tenant['client_id'],
                                     tenant['client_secret']).invoke().json()['access_token']
        for subscription in subscriptions:
            if subscription['offer_durable_id'] not in offer_durable_id_set:
                ratecard = AzureRatecard(credential,
                                         subscription['subscriptionId'],
                                         subscription['offer_durable_id'])
                azure_ratecard_collection.insert(ratecard.invoke().json()['Meters'],
                                                 check_keys=False)
                offer_durable_id_set.add(subscription['offer_durable_id'])

def refresh_usage_job():
    # TODO subprocess
    tenants = json.loads(AzureUtil.get_all_tenant())
    for tenant in tenants:
        subscriptions = json.loads(AzureUtil.get_all_subscription_by_tenant(tenant['tenant']))
        credential = AzureCredential(tenant['tenant'], tenant['client_id'],
                                     tenant['client_secret']).invoke().json()['access_token']
        reported_time = DatetimeUtil.get_start_and_end_datetime()
        for subscription in subscriptions:
            usage = AzureUsage(credential,
                               subscription['subscriptionId'],
                               reported_start_time=reported_time['reported_start_time'],
                               reported_end_time=reported_time['reported_end_time'])
            azure_usage_collection.insert(usage.invoke().json()['value'],
                                          check_keys=False)
            