from . import vkapi
import json


from .models import Dialog
from apps.social.models import VKAuth

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


def create_keyboard_for_block(labels, one_time=True):
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
        [{
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
        }]
    ]

    keyboard = {"one_time": one_time, "buttons": two_buttons_template}
    return json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def create_answer(data, token, dialog):
    user_id = data['user_id']
    payload = data['payload']

    print('create_answer ', data)

    # Default values
    message, attachment, keyboard = 'Непонятно', None, None

    # Пользователь первый раз начал переписку с сообществом
    if payload == '{"command":"start"}':
        # Создать диалог и выставить состояние, отправить приветствие, затем клавиатуру из двух кнопок
        # current_dialog = Dialog.objects.create_dialog(user_id)
        message = 'Привет! Ты только что нажал на кнопку старт! Давай решать задачи :)'
        keyboard = create_next_block_need_keyboard()

    vkapi.send_message(user_id, token, message, attachment, keyboard)
    print('exit create answer')


def create_dialog(user_id, token):
    print('handlers.py create_dialog')
    current_dialog = Dialog.objects.create_dialog(user_id)
    return current_dialog

def get_dialog(user_id, token):
    print('handlers.py get_dialog')
    try:
        current_dialog = Dialog.objects.get(user=VKAuth.objects.get(uid=str(user_id)).user)
        return current_dialog
    except Exception as e:
        print('get_dialog exception', e)


