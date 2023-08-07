import pymongo
from app.settings import load_config

config = load_config()
database_name = config.get('database_name', None)
collection_name = config.get('collection_name')


async def connect_to_mongodb(app):
    host = config['client'].get('host', 'localhost')
    port = config['client'].get('port', 27017)
    client = pymongo.MongoClient(host, port)
    app['mongo_client'] = client
    app['db'] = app['mongo_client'][database_name]
    app['collection'] = app['db'][collection_name]