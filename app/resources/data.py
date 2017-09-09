import json
from flask import request
from flask_restful import Resource, reqparse
from config import tenant_collection, subscription_collection, subscription_group_collection
from ..services.azure import AzureCredential, AzureRatecard, AzureUsage
from bson.json_util import dumps
from ..common.util import AzureUtil, DatetimeUtil
from datetime import timedelta

class Subscriptions(Resource):
    def get(self, tenant=None):
        return dumps(subscription_collection.find({"tenant": tenant},
                                                  {"subscriptionId": 1,
                                                   "_id": 0}))

class HistoryDataImport(Resource):
    def post(self):
        tenant = request.form['tenant']
        subscription = request.form['subscription']
        start = DatetimeUtil.datetime_converter(request.form['startDate'], request.form['startTime'])
        end = DatetimeUtil.datetime_converter(request.form['endDate'], request.form['endTime'])
        tenant_detail = json.loads(AzureUtil.get_tenant(tenant))
        print(tenant_detail)
        credential = AzureCredential(tenant_detail['tenant'], tenant_detail['client_id'],
                                     tenant_detail['client_secret']).invoke().json()['access_token']
        while start < end:
            temp = (start + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
            usage = AzureUsage(credential,
                               subscription,
                               reported_start_time=start.isoformat(),
                               reported_end_time=temp.isoformat())
            for document in usage.invoke().json()['value']:
                ratecard = azure_ratecard_collection.find_one({"MeterId": document['properties']['meterId']})
                # TODO exact calculation
                document['cost'] = document['properties']['quantity'] * ratecard['MeterRates']['0']
                azure_usage_collection.insert(document, check_keys=False)
            start = temp
            print(start, end)
