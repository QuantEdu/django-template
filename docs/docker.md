# Docker

Docker позволяет удобно и быстро разворачивать проекты для разработки и продакшена

Для установки нужно прочитать [официальную документацию](https://docs.docker.com)

Docker запускает отдельные контейнеры для каждой технологии. в нашем проекте это:

* Nginx
* PostgreSQL
* Python

Для большего удобства применяется надстройка над Docker - [docker-compose](https://docs.docker.com/compose/django/#connect-the-database)

Каждый контейнер описан в файле docker-compose.yml

## Команды docker

1. `docker stop $(docker ps -a -q)` - останавливает все docker процессы на компьютере
2. `docker rm $(docker ps -a -q)` - удаляет все docker процессы на компьютере
3. `docker ps` - показывает все запущенные на компьютере контейнеры
4. `docker-machine ls` - показывает список всех запущенных на компьютере машин
5. `docker-machine create -d virtualbox [machine_name];` - создает новую виртуальную машину с выбранным именем
6. `eval $(docker-machine env [machine_name])` - создает указатель для консоли на виртуальную машину
7. `docker-machine ip [machine_name]` - показывает список IP, связанных с данной машиной

## Команды docker-compose

1. `docker-compose up [-d] [--build]` - билдит и запускает контейнеры, описаные в docker-compose.yml
2. `docker-compose run [container_name] [command]` - запускает процесс в выбранном контейнере
3. `docker-compose stop` - останавливает контейнеры
4. `docker-compose down` --volumes - удаляет контейнеры и все созданные ими файлы

## Тематические статьи

### Docker-django quickstart from [Docker.com](https://docs.docker.com/compose/django/)