# Используйте официальный образ Python 3.10.11
FROM python:3.10.11

# Создайте директорию приложения
WORKDIR /app

# Копируйте зависимости и Pipfile.lock для установки зависимостей
COPY Pipfile Pipfile.lock config.yaml /app/

# Установите Pipenv
RUN pip install pipenv

# Установите зависимости с использованием Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Копируйте все остальные файлы приложения
COPY . /app/

# Запустите ваше приложение
CMD ["pipenv", "run", "python", "app.py"]
