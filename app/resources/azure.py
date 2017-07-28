from flask_restful import Resource
import requests

class Oauth(Resource):

    def post(self):
        """get access token
        """
        url = 'https://login.microsoftonline.com/472613e3-303b-4ae2-afc6-6a3b2d920675/ \
                oauth2/token?api-version=1.0'
        header = {
            "Content-Type" : "application/x-www-form-urlencoded"
        }
        payload = {
            "grant_type" : "client_credentials", \
            "resource" : "https://management.core.windows.net/", \
            "client_id" : "e4ec2c26-7b68-4b31-9665-b6cdeceb78a3", \
            "client_secret" : "tD0HJEdnovFZ9ytAINVsDZnriebhLZuGtrv46W2y0g8="
        }

        response = requests.post(url, data=payload, headers=header)

        return response

class Usage(Resource):

    def get(self):
        return 'guanpu'

    def post(self):
        pass

class Ratecard(Resource):

    def get(self):
        return 'guanpu'

    def post(self):
        pass