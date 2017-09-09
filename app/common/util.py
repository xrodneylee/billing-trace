from config import tenant_collection, subscription_collection,\
                   subscription_group_collection, azure_ratecard_collection
from bson.json_util import dumps
from datetime import datetime, timezone, timedelta, date, time

class AzureUtil():

    @staticmethod
    def get_all_tenant():
        return dumps(tenant_collection.find({}, {"_id": 0}))

    @staticmethod
    def get_tenant(tenant):
        return dumps(tenant_collection.find({"tenant": tenant}, {"_id": 0}))

    @staticmethod
    def get_all_subscription_by_tenant(tenant):
        return dumps(subscription_collection.find({"tenant": tenant}, {"subscriptionId": 1,
                                                                       "offer_durable_id": 1,
                                                                       "_id": 0}))

class DatetimeUtil():

    @staticmethod
    def get_start_and_end_datetime():
        tz = timezone(offset=timedelta(hours=8), name='Asia/Taipei')
        return {
            "reported_start_time": ((datetime.now(timezone.utc).astimezone(tz) - timedelta(hours=2))
                                    .replace(minute=0, second=0, microsecond=0)).isoformat(),
            "reported_end_time": ((datetime.now(timezone.utc).astimezone(tz) - timedelta(hours=1))
                                  .replace(minute=0, second=0, microsecond=0)).isoformat()
        }

    @staticmethod
    def datetime_converter(date_str, time_str):
        tz = timezone(offset=timedelta(hours=8), name='Asia/Taipei')
        year, month, day = (int(item) for item in date_str.split('-'))
        hour, minutes = (int(item) for item in time_str.split(':'))
        d = date(year, month, day)
        t = time(hour, minutes, tzinfo=tz)
        return datetime.combine(d, t).replace(minute=0, second=0, microsecond=0)
