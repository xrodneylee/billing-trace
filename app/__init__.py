from flask import Flask, render_template
from flask_restful import Api
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from .resources.mock import Mock
from .resources.settings import Tenant, Subscription, Group
from .resources.data import Subscriptions, HistoryDataImport
from .jobs.import_data import refresh_ratecard_job, refresh_usage_job


app = Flask(__name__)
api = Api(app)


# restful api
api.add_resource(Mock, '/mock')
api.add_resource(Tenant, '/setting/tenant', '/setting/tenant/<tenant>')
api.add_resource(Subscription, '/setting/subscription', '/setting/subscription/<subscription>')
api.add_resource(Group, '/setting/group', '/setting/group/<group_name>')
api.add_resource(Subscriptions, '/data/<tenant>/subscriptions')
api.add_resource(HistoryDataImport, '/data/import')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# scheduler
sched = BackgroundScheduler()
sched.add_job(refresh_ratecard_job, 'cron', hour=3)
sched.add_job(refresh_usage_job, 'cron', minute=40)
sched.start()

# backend
from .views import general

app.register_blueprint(general.mod)
