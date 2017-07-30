from flask_restful import Resource, reqparse
from config import db

parser = reqparse.RequestParser(trim=True)
parser.add_argument('tenant', required=True, type=str, help='tenant cannot be blank')

tenant_collection = db['tenant']

class Tenant(Resource):

    def get(self):
        """get single/all tenant
        """
        return NotImplemented

    def post(self):
        """create new tenant
        """
        args = parser.parse_args()

        if tenant_collection.find_one({"tenant": args['tenant']}):
            return {"response": "tenant already exists."}
        else:
            tenant_collection.insert_one({'tenant': args['tenant']})
            return {'tenant': args['tenant']}

    def delete(self):
        """delete tenant
        """
        return NotImplemented

    def put(self):
        """update tenant
        """
        return NotImplemented
