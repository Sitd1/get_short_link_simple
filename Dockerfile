# Используйте базовый образ Python
FROM python:3.9

# Устанавливаем необходимые системные пакеты
RUN apt-get update && apt-get install -y \
    python3.10-dev \
    && rm -rf /var/lib/apt/lists/*

# Создайте директорию приложения
WORKDIR /app

# Копируйте зависимости и Pipfile.lock для установки зависимостей
COPY Pipfile Pipfile.lock /app/

# Установите Pipenv
RUN pip install pipenv

# Установите зависимости с использованием Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Копируйте все остальные файлы приложения
COPY . /app/

# Запустите ваше приложение
CMD ["pipenv", "run", "python", "app.py"]
