from aiohttp import web
from shortener import Shortener
from swagger import setup_swagger

app = web.Application()

# Настройка MongoDB
app['mongo'] = 'mongodb://localhost:27017'
app['db_name'] = 'shortener'
app['collection_name'] = 'links'

# Инициализация объекта для сокращения и расширения ссылок
shortener = Shortener(app)

# Настройка Swagger
setup_swagger(app)

# Обработчик для сокращения ссылки
async def shorten(request):
    data = await request.json()
    long_url = data.get('long_url')
    if not long_url:
        return web.json_response({'error': 'Missing long_url parameter'}, status=400)
    short_url = shortener.shorten(long_url)
    return web.json_response({'short_url': short_url})

# Обработчик для расширения ссылки
async def expand(request):
    short_url = request.match_info.get('short_url')
    if not short_url:
        return web.json_response({'error': 'Missing short_url parameter'}, status=400)
    long_url = shortener.expand(short_url)
    if not long_url:
        return web.json_response({'error': 'Short URL not found'}, status=404)
    return web.json_response({'long_url': long_url})

app.router.add_post('/shorten', shorten)
app.router.add_get('/expand/{short_url}', expand)

if __name__ == '__main__':
    web.run_app(app)
