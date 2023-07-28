import pymongo

async def connect_to_mongodb(app):
    app['mongo_client'] = pymongo.MongoClient("mongodb://localhost:27017/")
    app['db'] = app['mongo_client']["short_links"]
    app['collection'] = app['db']["links"]
