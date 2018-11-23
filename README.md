![Logo of the project](./images/logo.sample.png)

# Quant
> Приложение для дистанционного образования. И еще наш сайт.

Quant создается как электронная платформа для нашего учебного центра.

Может быть доступна из браузеров и при помощи бота в Telegram.

## Installing / Getting started

Проект легко разворачивается при помощи docker-compose

```shell
docker-compose build
docker-compose up
```

После чего сайт будет доступен по IP docker-machine или по `localhost`

## Структура проекта

```
django-template
├─ .envs (переменные окружения)
├─ docker (Все Dockerfile для сборки проекта)
├─ docs (документация проекта и используемых технологий)
├─ web (Python+Django-приложение)
├─ .env Файл с переменными окружения
└─ docker-compose.yml (сборка и запуск docker-контейнеров)
```

## Developing

### Built With
- Python
- Django
- Docker
- Bootstrap4

### Prerequisites
Для начала разработки необходимо установить Docker на свой компьютер. [официальная документация](https://docs.docker.com)
В дальнейшем рекомендуется использовать IDE PyCharm.
На компьютере необходимо установить локально Postgres последней версии и Python3.6.


### Setting up Dev

Консольные команды, которые необходимо выполнить:

```shell
git clone https://github.com/QuantEdu/quant.git
cd quant/
docker-compose -f local.yml up
```

Для работы в Pycharm:
1. В PyCharm - Settings - Build - Docker. Создать указатель на docker-machine с полным путем до docker-compose
2. Создать remote interpreter для проекта, запускающий docker-compose
3. Создать run\debug конфигурацию, которая собирает при помощи файла docker-compose.yml
4. Запускать docker-machine через специальную вкладку и деплоить по инструкции из docker-compose

## Deploy

Проект деплоится на http://quant.study
```
IP-адрес: 188.127.249.128
Пользователь: root
Пароль: oGWRAKrle8so
```



> By [project-guideline](https://github.com/wearehive/project-guidelines/blob/master/README.sample.md)

