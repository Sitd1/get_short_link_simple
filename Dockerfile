# Используем официальный образ Python 3.10.11
FROM python:3.10.11

# Назначаем рабочую дирректорию
WORKDIR /shortener_app

# Копируем зависимости и Pipfile.lock для последующей установки
COPY Pipfile Pipfile.lock config.yaml ./

# Устанавливаем Pipenv
RUN pip install pipenv

# Устанавливаем зависимости с использованием Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Назначаем директорию приложения с основным кодом
WORKDIR /shortener_app/app

# Копируем все остальные файлы приложения
COPY app /shortener_app/app/

# Запускаем приложение приложение
CMD ["pipenv", "run", "python", "app.py"]
