from ..services.azure import AzureCredential, AzureRatecard, AzureUsage
from config import db
from bson.json_util import dumps
import configparser

tenants = {}
subscriptions = {}
azure_ratecard_collection = db['azure-ratecard']

def get_ratecard():
    config = configparser.ConfigParser()
    config.read_file(open("secret.properties"))

    tenant = config.get("Azure", "tenant")
    client_id = config.get("Azure", "client_id")
    client_secret = config.get("Azure", "client_secret")
    subscription = config.get("Azure", "subscription")
    offer_durable_id = config.get("Azure", "offer_durable_id")

    credential = AzureCredential(tenant, client_id, client_secret)
    ratecard = AzureRatecard(credential.invoke().json()['access_token'],
                             subscription,
                             offer_durable_id)
    # for document in ratecard.invoke().json()['Meters']:
    azure_ratecard_collection.remove({})
    azure_ratecard_collection.insert(ratecard.invoke().json()['Meters'], check_keys=False)
    # print(ratecard.invoke().json())
