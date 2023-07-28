from aiohttp import web
import aiohttp_jinja2

async def show_form(request):
    return aiohttp_jinja2.render_template('index.html', request, {})

async def create_short_link(request):
    # Ваш код обработки создания короткой ссылки

    # Вернуть результат обработки
    # Например:
    return web.HTTPFound('/result')
