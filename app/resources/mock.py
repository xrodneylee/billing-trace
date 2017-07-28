from flask_restful import Resource

class mock(Resource):

    def get(self):
        return 'guanpu'

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass