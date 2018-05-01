from . import vkapi
import apiai
import json


DIALOG_FLOW_TOKEN = '281dbfa163e343fdba0368f4857c84d4'

def create_answer(data, token):
    user_id = data['user_id']
    body = data['body'].lower()

    # Default values
    message, attachment = 'Непонятно', ''

    print(body)

    if body in ['help', 'помощь']:
        message = 'Привет, я новый бот! Ты выбрал команду help'
    elif body in ['задача']:
        message = 'Привет, я новый бот! Ты выбрал команду задача'
        attachment = 'photo-165396328_456239018'
    else:
        request = apiai.ApiAI(DIALOG_FLOW_TOKEN).text_request()  # Токен API к Dialogflow
        request.lang = 'ru'  # На каком языке будет послан запрос
        request.session_id = user_id  # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.query = body  # Посылаем запрос к ИИ с сообщением от юзера
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
        if response:
            message = response
        else:
            message = 'Привет, я новый бот! Я тебя не понял. Поэтому не шли мне больше {}'.format(body)
    vkapi.send_message(user_id, token, message, attachment)