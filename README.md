# django-template

## Структура проекта

```
django-template
├─ django (Python+Django-приложение)
├─ docker (Все Dockerfile для сборки проекта)
├─ docs (документация проекта)
└─ docker-compose.yml (сборка и запуск docker-контейнеров)
```

Для начала работы нужно:
1. Установить Docker на компьютер. [официальная документация](https://docs.docker.com)
2. `docker-compose build && docker-compose up`

или

1. В PyCharm - Settings - Build - Docker. Создать указатель на docker-machine с полным путем до docker-compose
2. Создать remote interpreter для проекта, запускающий docker-compose

Для пересборки проекта
1. `docker-compose stop && docker-compose rm -f && docker-compose build --no-cache && docker-compose up -d`

Настройка окружения в PyCharm. [как получить бесконечную лицензию](https://vk.com/@maxstern-getting-rid-of-jetbrains-license-crap-forever)
1. Открыть проект
2. Узнать IP docker-machine - это будет ip хоста
3. подключиться к БД используя данные из .env файла
4. Консоль ассоциировать c docker-machine при помощи `eval $(docker-machine env default)`

## Работа с данными
1. `sudo docker exec djangotemplate_db_1 pg_dump -U postgres postgres > pg_backups/postgres_$(date +%Y-%m-%d).sql`


## TO-DO'S:
- backup postgres data
- [connect uwsgi instance](https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/) [Docs](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
- use pg_dump automatically [pg_dump](https://github.com/istepanov/docker-pg_dump)
