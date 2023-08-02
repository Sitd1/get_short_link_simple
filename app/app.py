import uuid
import aiohttp_swagger
from aiohttp import web
import pymongo
from app.url_shortener.utils import generate_short_url


# Подключение к базе данных MongoDB


mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["url_shortener"]
collection = db["urls"]


# Обработчик для загрузки веб-страницы
async def index(request):
    with open('templates/index.html', 'r') as file:
        content = file.read()
    return web.Response(text=content, content_type='text/html')

# Обработчик для создания короткой ссылки
async def create_short_url(request):
    data = await request.json()
    original_url = data.get("original_url")

    if not original_url:
        return web.json_response({"error": "Original URL is required"}, status=400)

    # Проверка, есть ли уже запись в базе данных для данной оригинальной ссылки
    existing_url = collection.find_one({"original_url": original_url})
    if existing_url:
        return web.json_response({"short_url": existing_url["short_url"], "request_count": existing_url["request_count"]})

    # Генерируем короткую ссылку
    short_url = generate_short_url()

    # Сохраняем запись в базе данных
    collection.insert_one({"original_url": original_url, "short_url": short_url, "request_count": 0})

    return web.json_response({"short_url": short_url, "request_count": 0})

# Обработчик для получения оригинальной ссылки по короткой ссылке
async def get_original_url(request):
    short_url = request.match_info["short_url"]

    # Ищем запись в базе данных по короткой ссылке
    url_data = collection.find_one({"short_url": short_url})

    if not url_data:
        return web.json_response({"error": "Short URL not found"}, status=404)

    # Увеличиваем счетчик запросов и обновляем запись в базе данных
    collection.update_one({"short_url": short_url}, {"$inc": {"request_count": 1}})

    return web.json_response({"original_url": url_data["original_url"], "request_count": url_data["request_count"]})

# Настройка сервера и маршрутов
app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/shorten', create_short_url)
app.router.add_get('/{short_url}', get_original_url)

# Настройка Swagger
aiohttp_swagger.setup_swagger(
    app=app,
    swagger_url='/swagger',
    ui_version=3,
    swagger_from_file='swagger.yaml'
)

# Настройка статических файлов
app.router.add_static('/static/', path='static', name='static')

web.run_app(app)


if __name__ ==  "__main__":
    web.run_app(app)