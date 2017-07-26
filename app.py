# Copyright (c) 2017, Lee Guan Pu
# All rights reserved.

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
api = Api(app)