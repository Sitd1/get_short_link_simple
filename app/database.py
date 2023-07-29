import pymongo
from utils import load_config

config = load_config()

# async def connect_to_mongodb(app):
#     client_ = config['client'].replace('<username>', config['user']).replace('<password>', config['password'])
#     client = pymongo.MongoClient(client_)
#     app['mongo_client'] = client
#     app['db'] = app['mongo_client']["short_links"]
#     app['collection'] = app['db']["links"]


if __name__ == '__main__':
    client_ = config['client'].replace('<username>', config['user']).replace('<password>', config['password'])
    client = pymongo.MongoClient(client_)
    db = client.test
    coll = db.new_users
    coll.insert_one({"id": 1, "name": 'Apex'})
    print('ok')


