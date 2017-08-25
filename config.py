import logging, logging.config
import pymongo

client = pymongo.MongoClient("mongodb://xrodneylee:xrodneylee@" \
                                       + "cluster0-shard-00-00-5ekni.mongodb.net:27017," \
                                       + "cluster0-shard-00-01-5ekni.mongodb.net:27017," \
                                       + "cluster0-shard-00-02-5ekni.mongodb.net:27017/admin?" \
                                       + "ssl=true&replicaSet=Cluster0-shard-0&authSource=admin")
# database
db = client['azure-billing']

# collections
tenant_collection = db['tenant']
subscription_collection = db['subscription']
subscription_group_collection = db['subscription-group']
azure_ratecard_collection = db['azure-ratecard']
azure_usage_collection = db['azure-usage']


# logging
LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simpleFormatter',
            'filename': 'azure-billing.log',
            'maxBytes': 1024,
            'backupCount': 3
        }
    },
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'loggers': {
        'azure_billing': {
            'level': 'DEBUG',
            'handlers': ['file']
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger('azure_billing')
