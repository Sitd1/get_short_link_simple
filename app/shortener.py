import shortuuid

class Shortener:
    def __init__(self, app):
        self.collection = app['db'][app['collection_name']]

    async def shorten(self, long_url):
        # Генерируем короткий идентификатор
        short_id = shortuuid.ShortUUID().random(length=6)
        # Сохраняем ссылку в базе данных
        await self.collection.insert_one({'short_url': short_id, 'long_url': long_url, 'clicks': 0})
        return short_id

    async def expand(self, short_url):
        link = await self.collection.find_one({'short_url': short_url})
        if link:
            # Увеличиваем счетчик переходов
            await self.collection.update_one({'short_url': short_url}, {'$inc': {'clicks': 1}})
            return link['long_url']
        return None
