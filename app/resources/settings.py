""" azure settings """
from flask_restful import Resource, reqparse
from config import db
from bson.json_util import dumps

parser = reqparse.RequestParser(trim=True)
parser.add_argument('tenant', required=True, type=str, help='tenant cannot be blank')

tenant_collection = db['tenant']
subscription_collection = db['subscription']

class Tenant(Resource):
    """
    Tenant restful api
    """
    def get(self, tenant=None):
        """get single/all tenant
        """
        if tenant:
            return dumps(tenant_collection.find_one({"tenant": tenant}, {"_id": 0}))
        else:
            return dumps(tenant_collection.find({}, {"_id": 0}))

    def post(self):
        """create new tenant
        """
        args = parser.parse_args()

        if tenant_collection.find_one({"tenant": args['tenant']}):
            return {"response": "tenant already exists."}
        else:
            tenant_collection.insert_one({'tenant': args['tenant']})
            return dumps(tenant_collection.find_one({"tenant": args['tenant']}, {"_id": 0}))

    def delete(self, tenant=None):
        """delete tenant
        """
        if tenant:
            tenant_collection.delete_one({"tenant": tenant})

    def put(self):
        """update tenant
        """
        return NotImplemented

class Subscription(Resource):
    pass