import aiohttp_swagger
from aiohttp import web
import pymongo
from url_shortener.utils import generate_short_url
from settings import load_config
# from database import connect_to_mongodb

config = load_config()

# Подключение к базе данных MongoDB

mongo_client = pymongo.MongoClient(f"mongodb://localhost:27017/")
db = mongo_client["url_shortener"]
collection = db["urls"]


# Обработчик для загрузки веб-страницы
async def index(request):
    with open('templates/index.html', 'r') as file:
        content = file.read()
    return web.Response(text=content, content_type='text/html')


# Функция для создания короткой ссылки
async def create_short_url(request):
    data = await request.json()
    posted_url = data.get("original_url")

    if not posted_url:
        return web.json_response({"error": "Original URL is required"}, status=400)

    # Проверка, есть ли уже запись в базе данных для данной оригинальной ссылки
    existing_orig_url = collection.find_one({"original_url": posted_url})
    exitinig_short_url = collection.find_one({"short_url": posted_url})
    if existing_orig_url:
        return web.json_response({"short_url": existing_orig_url["short_url"], "request_count": existing_orig_url["request_count"]})
    elif exitinig_short_url:
        # Проверка, есть ли уже запись в базе данных для короткой ссылки
        return web.json_response({"short_url": exitinig_short_url["original_url"], "request_count": exitinig_short_url["request_count"]})

    # Генерируем короткую ссылку
    short_url = generate_short_url(length=config['short_link_length'])

    # Сохраняем запись в базе данных
    collection.insert_one({"original_url": posted_url, "short_url": short_url, "request_count": 0})

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
    print(url_data)

    return web.json_response({"original_url": url_data["original_url"], "request_count": url_data["request_count"]})



# Обработчик для перехода по короткой ссылке
async def redirect_short_url(request):
    short_url = request.match_info["short_url"]

    # Ищем запись в базе данных по короткой ссылке
    url_data = collection.find_one({"short_url": short_url})

    if not url_data:
        return web.json_response({"error": "Short URL not found"}, status=404)

    # Увеличиваем счетчик переходов и обновляем запись в базе данных
    collection.update_one({"short_url": short_url}, {"$inc": {"request_count": 1}})

    # Выполняем редирект на оригинальную ссылку
    return web.HTTPFound(url_data["original_url"])


# Настройка сервера и маршрутов
app = web.Application()
app.router.add_get('/', index)
app.router.add_post('/shorten', create_short_url)
app.router.add_get('/{short_url}', redirect_short_url)
app.router.add_post('/{short_url}', get_original_url)

# app.router.add_get('/{short_url}', get_original_url)
# app.router.add_get('/r/{short_url}', redirect_short_url)  # Добавлен новый маршрут для перехода по короткой ссылке


# Настройка Swagger
aiohttp_swagger.setup_swagger(app=app, **config['setup_swagger'])

# Настройка статических файлов
app.router.add_static('/static/', path='static', name='static')

if __name__ == "__main__":
    web.run_app(app)
