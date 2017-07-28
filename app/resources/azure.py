from flask_restful import Resource

# https://login.microsoftonline.com/<tenant>/oauth2/token?api-version=1.0
class Oauth(Resource):

    root_url = 'https://login.microsoftonline.com'
    oauth2_path = 'OAuth2/Token'
    api_version_key = 'api-version'
    api_version_value = '1.0'
    post_grant_type = 'client_credentials'
    post_resource = 'https://management.core.windows.net/'

    def get(self):
        return 'guanpu'

    def post(self):
        pass

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