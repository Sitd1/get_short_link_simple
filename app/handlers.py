

class handler:
    def __init__(self):
        pass

    # Обработчик для загрузки веб-страницы
    async def index(self, request):
        with open('templates/index.html', 'r') as file:
            content = file.read()
        return web.Response(text=content, content_type='text/html')


    # Функция для создания короткой ссылки
    async def create_short_url(self, request):
        data = await request.json()
        original_url = data.get("original_url")

        if not original_url:
            return web.json_response({"error": "Original URL is required"}, status=400)

        # Проверка, есть ли уже запись в базе данных для данной оригинальной ссылки
        existing_url = collection.find_one({"original_url": original_url})
        if existing_url:
            return web.json_response({"short_url": existing_url["short_url"], "request_count": existing_url["request_count"]})

        # Генерируем короткую ссылку
        short_url = generate_short_url(length=config['short_link_length'])

        # Сохраняем запись в базе данных
        collection.insert_one({"original_url": original_url, "short_url": short_url, "request_count": 0})

        return web.json_response({"short_url": short_url, "request_count": 0})


    # Обработчик для получения оригинальной ссылки по короткой ссылке
    async def get_original_url(self, request):
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
    async def redirect_short_url(self, request):
        short_url = request.match_info["short_url"]

        # Ищем запись в базе данных по короткой ссылке
        url_data = collection.find_one({"short_url": short_url})

        if not url_data:
            return web.json_response({"error": "Short URL not found"}, status=404)

        # Увеличиваем счетчик переходов и обновляем запись в базе данных
        collection.update_one({"short_url": short_url}, {"$inc": {"request_count": 1}})

        # Выполняем редирект на оригинальную ссылку
        return web.HTTPFound(url_data["original_url"])