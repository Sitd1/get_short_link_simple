import re
import uuid


def is_valid_url(url) -> bool:
    # Регулярное выражение для проверки формата URL
    pattern = r'^(https?|ftp)://[^\s/$.?#].[^\s]*$'
    # Проверяем, соответствует ли ссылка формату URL
    if re.match(pattern, url):
        return True
    else:
        return False


def generate_short_url(length: int = 8) -> str:
    # UUID  Generation
    short_link = str(uuid.uuid4()).replace('-', '')[:length]
    return short_link