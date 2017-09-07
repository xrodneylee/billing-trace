from flask import request
from flask_restful import Resource, reqparse
from config import tenant_collection, subscription_collection, subscription_group_collection
from bson.json_util import dumps
from ..common.util import DatetimeUtil

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
        print(start, end)
