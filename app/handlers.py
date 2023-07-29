from aiohttp import web
import aiohttp_jinja2
from pymongo import collection
from create_short_link import generate_short_link


async def show_form(request):
    return aiohttp_jinja2.render_template('index.html', request, {})


async def create_short_link(request):
    # Получить длинную ссылку из входящего запроса
    long_link = request.rel_url.query.get('long_link')

    # Проверить, не существует ли уже короткая ссылка для данной длинной ссылки в базе данных
    existing_link = collection.find_one({'long_link': long_link})
    if existing_link:
        return web.json_response({'short_link': existing_link['short_link']})

    # Сгенерировать короткую ссылку (например, с помощью UUID)
    short_link = generate_short_link()

    # Сохранить данные в базе данных
    collection.insert_one({'long_link': long_link, 'short_link': short_link, 'clicks': 0})

    return web.json_response({'short_link': short_link})


async def get_long_link(request):
    # Получить короткую ссылку из входящего запроса
    short_link = request.rel_url.query.get('short_link')
    # Найти запись с данной короткой ссылкой в базе данных
    link = collection.find_one({'short_link': short_link})
    if not link:
        return web.json_response({'error': 'Short link not found'}, status=404)

    # # Увеличить счетчик кликов
    # collection.update_one({'short_link': short_link}, {'$inc': {'clicks': 1}})

    # Вернуть истинную длинную ссылку
    return web.json_response({'long_link': link['long_link']})


async def get_statistics(request):
    # Получить короткую ссылку из входящего запроса
    short_link = request.rel_url.query.get('short_link')

    # Найти запись с данной короткой ссылкой в базе данных
    link = collection.find_one({'short_link': short_link})
    if not link:
        return web.json_response({'error': 'Short link not found'}, status=404)

    # Вернуть статистику
    return web.json_response({'short_link': short_link, 'clicks': link['clicks']})
