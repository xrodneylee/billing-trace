import requests

class Oauth:

    def __init__(self, tenant=None, client_id=None, client_secret=None):
        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret

    def invoke(self):
        """get access token
        """
        url = 'https://login.microsoftonline.com/' + self.tenant + '/oauth2/token'
        header = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        params = {
            "api-version" : '1.0'
        }
        data = {
            "grant_type" : "client_credentials",
            "resource" : "https://management.core.windows.net/",
            "client_id" : self.client_id,
            "client_secret" : self.client_secret
        }

        response = requests.post(url, params=params, headers=header, data=data)

        return response

class Usage():

    def __init__(self, tenant=None, client_id=None, client_secret=None):
        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret

    def invoke(self):
        
        oauth = Oauth(self.tenant, self.client_id, self.client_secret)
        token = oauth.invoke().json()['access_token']

        url = 'https://management.azure.com/ \
                subscriptions/08baa038-b64f-49f0-a084-7c22d1c1305c/ \
                providers/Microsoft.Commerce/UsageAggregates'
        header = {
            "Content-Type" : "application/json",
            "Authorization" : "Bearer " + token
        }
        params = {
            "api-version" : '2015-06-01-preview',
            "reportedStartTime" : "2017-03-22T00%3a00%3a00%2b00%3a00",
            "reportedEndTime" : "2017-03-23T00%3a00%3a00%2b00%3a00",
            "aggregationGranularity" : "Hourly",
            "showDetails" : "true"
        }

        response = requests.post(url, params=params, headers=header)

        return response

class Ratecard():

    def get(self):
        return 'guanpu'

    def post(self):
        pass