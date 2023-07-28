from aiohttp import web
import aiohttp_jinja2
import jinja2
from app.handlers import show_form, create_short_link
from app.database import connect_to_mongodb

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('app/templates'))

app.router.add_get('/', show_form)
app.router.add_post('/create_short_link', create_short_link)

# Здесь подключите ваш Swagger, если вы его используете

# Подключение к MongoDB
app.on_startup.append(connect_to_mongodb)

web.run_app(app)
