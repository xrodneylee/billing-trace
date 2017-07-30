from flask_restful import Resource, reqparse
# from .. import db

parser = reqparse.RequestParser(trim=True)
parser.add_argument('tenant', required=True, type=str, help='tenant cannot be blank')

class Tenant(Resource):

    def get(self):
        return 'guanpu'

    def post(self):
        args = parser.parse_args()
        return {'tenant': args['tenant']}

    def delete(self):
        pass

    def put(self):
        pass
