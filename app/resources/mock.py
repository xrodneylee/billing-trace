from flask_restful import Resource
from config import db

class Mock(Resource):

    def get(self):
        return 'guanpu'

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass