from aiohttp_swagger import setup_swagger

def setup_swagger(app):
    setup_swagger(
        app=app,
        swagger_url='/api/doc',
        description='Shortener API',
        title='Shortener',
    )
