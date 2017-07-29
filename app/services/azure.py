import requests

class AzureCredential:

    def __init__(self, tenant=None, client_id=None, client_secret=None):
        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret

    def invoke(self):
        """get access token
        """
        url = 'https://login.microsoftonline.com/' + self.tenant + '/oauth2/token'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {
            'api-version': '1.0'
        }
        data = {
            'grant_type': 'client_credentials',
            'resource': 'https://management.core.windows.net/',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }

        response = requests.post(url, params=params, headers=header, data=data)

        return response

class AzureUsage():

    def __init__(self, token=None, subscription=None):
        self.token = token
        self.subscription = subscription

    def invoke(self):
        url = 'https://management.azure.com/subscriptions/' \
                + self.subscription \
                + '/providers/Microsoft.Commerce/UsageAggregates'
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }
        params = {
            'api-version': '2015-06-01-preview',
            'reportedStartTime': '2017-03-22T00:00:00+00:00',
            'reportedEndTime': '2017-03-23T00:00:00+00:00',
            'aggregationGranularity': 'Hourly',
            'showDetails': 'true'
        }

        response = requests.get(url, params=params, headers=header)

        return response

class AzureRatecard():

    def __init__(self, token=None, subscription=None, offer_durable_id=None,
                 currency='TWD', locale='zh-TW', region_info='TW'):
        self.token = token
        self.subscription = subscription
        self.offer_durable_id = offer_durable_id # MS-AZR-0025P
        self.currency = currency
        self.locale = locale
        self.region_info = region_info

    def invoke(self):
        url = 'https://management.azure.com/subscriptions/' \
                + self.subscription \
                + '/providers/Microsoft.Commerce/RateCard'
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.token
        }
        params = {
            'api-version': '2016-08-31-preview',
            '$filter': "OfferDurableId eq '{offer_durable_id}' \
                        and Currency eq '{currency}' \
                        and Locale eq '{locale}' \
                        and RegionInfo eq '{region_info}' " \
            .format(
                offer_durable_id=self.offer_durable_id,
                currency=self.currency,
                locale=self.locale,
                region_info=self.region_info
            )
        }

        response = requests.get(url, params=params, headers=header)

        return response


# test
credential = AzureCredential('472613e3-303b-4ae2-afc6-6a3b2d920675', 'e4ec2c26-7b68-4b31-9665-b6cdeceb78a3', 'tD0HJEdnovFZ9ytAINVsDZnriebhLZuGtrv46W2y0g8=')
ratecard = AzureRatecard(credential.invoke().json()['access_token'], '08baa038-b64f-49f0-a084-7c22d1c1305c', 'MS-AZR-0025P')
print(ratecard.invoke().text)
