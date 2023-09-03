FROM python:3.10

# Устанавливаем pipenv внутри контейнера
RUN pip install pipenv

# Создаем и устанавливаем директорию приложения внутри контейнера
WORKDIR /app

# Копируем Pipfile и Pipfile.lock в контейнер
COPY Pipfile Pipfile.lock /app/

# Устанавливаем зависимости с помощью pipenv
RUN pipenv install --deploy --ignore-pipfile

# Копируем остальные файлы вашего приложения в контейнер
COPY . /app/

# Команда для запуска вашего приложения (замените на вашу команду)
CMD ["pipenv", "run", "python", "app.py"]
