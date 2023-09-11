# get_short_link_simple

Сервис, который принимает длинную ссылку и возвращает короткую ссылку.

## Оглавление

- [Описание](#описание)
- [Установка](#установка)
- [Использование](#использование)

## Описание

Сервис (на aiohttp), который принимает длинную ссылку и возвращает короткую ссылку. 
Также этот сервис может принять короткую ссылку и вернуть истинную длинную ссылку.
Если ссылка уже приходила, то возвращается, что и в предыдущий раз. 

## Установка

### Скачайте репозитории при помощи git

Используя SSH
```bash
git clone git@github.com:Sitd1/get_short_link_simple.git
```

Используя http:

```bash
git clone https://github.com/Sitd1/get_short_link_simple.git
```
### Разверните контейнеры при помощи docker-compose
Для этого должны быть предустановлены docker и docker-compose
* Перейдите в корневую дирректорию приложения get_short_link_simple, там должен лежать файл docker-compose.yml
* После того, как убедитесь в наличии файла в дирректории где вы сейчас находитесь используйте следующую команду, чтобы развернуть контейнеры
```bash
docker-compose up --build -d
```

### Использование
* перейдите на http://0.0.0.0:8080/ и вам будет доступен сервис
* появится поле ввода и кнопка
* в поле ввода можно ввести длинную ссылку
* нажать на кнопку "Shorten"
* снизу появится часть короткой ссылки вида "69e3822d"
* если добавить 69e3822d к http://0.0.0.0:8080/ и перейти по ссылке: http://0.0.0.0:8080/69e3822d, то будет перевод на длинную ссылку
* если хотите получить длинную ссылку на основе короткой, то просто в то же поле введите часть короткой ссылки, например, 69e3822d, то вернет длинную ссылку, к которой прикреплена короткая ссылка

## PS
Сервис будет по-тихому обновляться



