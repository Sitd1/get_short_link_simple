import motor.motor_asyncio

async def get_mongo_client(app):
    return motor.motor_asyncio.AsyncIOMotorClient(app['mongo'])

async def setup_mongo(app):
    app['mongo_client'] = await get_mongo_client(app)
    app['db'] = app['mongo_client'][app['db_name']]

async def close_mongo(app):
    app['mongo_client'].close()
