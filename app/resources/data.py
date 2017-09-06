from flask import request
from flask_restful import Resource, reqparse
from config import tenant_collection, subscription_collection, subscription_group_collection
from bson.json_util import dumps

class Subscriptions(Resource):
    def get(self, tenant=None):
        return dumps(subscription_collection.find({"tenant": tenant},
                                                  {"subscriptionId": 1,
                                                   "_id": 0}))

class HistoryDataImport(Resource):
    def post(self):
        tenant = request.form['tenant']
        subscription = request.form['subscription']
        start_date = request.form['startDate']
        start_time = request.form['startTime']
        end_date = request.form['endDate']
        end_time = request.form['endTime']
        print(tenant, subscription, start_date, start_time, end_date, end_time)
