from . import vkapi
import apiai
import json


from apps.users.models import Dialog

"""
Прмер клавиатуры, которая прилетает
{ 
"type":"message_new", 
"object":{ 
   "id":41, 
   "date":1526898082, 
   "out":0, 
   "user_id":163176673, 
   "read_state":0, 
   "title":"", 
   "body":"Blue", 
   "payload":"{\"button\":\"4\"}" 
  }, 
"group_id":1}
"""

DIALOG_FLOW_TOKEN = '281dbfa163e343fdba0368f4857c84d4' # ???


def create_keyboard_for_block(labels, one_time=False):
    four_buttons_template = [
        {
            "action": {
                "type": "text",
                "payload": "{\"option_button\": \"1\"}",
                "label": labels[0]
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"option_button\": \"2\"}",
                "label": labels[1]
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"option_button\": \"3\"}",
                "label": labels[2]
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"option_button\": \"4\"}",
                "label": labels[3]
            },
            "color": "default"
        }
    ]

    keyboard = {"one_time" : one_time, "buttons" : four_buttons_template}
    return json.dumps(keyboard)


def create_next_block_need_keyboard(one_time=False):
    two_buttons_template = [
        {
            "action": {
                "type": "text",
                "payload": "{\"next_block_button\": \"1\"}",
                "label": "Следующая задача"
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": "{\"next_block_button\": \"2\"}",
                "label": "На сегодня хватит"
            },
            "color": "default"
        }
    ]

    keyboard = {"one_time": one_time, "buttons": two_buttons_template}
    return json.dumps(keyboard)


def create_answer(data, token):
    user_id = data['user_id']
    payload = data['payload']

    print('create_answer ', data)

    # Default values
    message, attachment, keyboard = 'Непонятно', '', ''

    # Пользователь первый раз начал переписку с сообществом
    if payload == '{"command":"start"}':
        # Создать диалог и выставить состояние, отправить приветствие, затем клавиатуру из двух кнопок
        # current_dialog = Dialog.objects.create_dialog(user_id)
        message = 'Привет! Ты только что нажал на кнопку старт! Давай решать задачи :)'
        # keyboard = create_next_block_need_keyboard()

    # print(body)
    #
    # if body in ['help', 'помощь']:
    #     message = 'Привет, я новый бот! Ты выбрал команду help'
    # elif body in ['задача']:
    #     message = 'Привет, я новый бот! Ты выбрал команду задача'
    #     attachment = 'photo-165396328_456239018'
    # else:
    #     request = apiai.ApiAI(DIALOG_FLOW_TOKEN).text_request()  # Токен API к Dialogflow
    #     request.lang = 'ru'  # На каком языке будет послан запрос
    #     request.session_id = user_id  # ID Сессии диалога (нужно, чтобы потом учить бота)
    #     request.query = body  # Посылаем запрос к ИИ с сообщением от юзера
    #     responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    #     response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    #     if response:
    #         message = response
    #     else:
    #         message = 'Привет, я новый бот! Я тебя не понял. Поэтому не шли мне больше {}'.format(body)

    vkapi.send_message(user_id, token, message, attachment, keyboard)

