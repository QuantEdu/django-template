from . import vkapi
import json
import sys
import traceback

# from django_postgres_extensions.models.expressions import Index

from .models import Dialog
from apps.social.models import UserSocialAuth
from apps.studio.blocks import ChoiceBlock, ChoiceBlockOption
from apps.lms.results import ChoiceBlockResult

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
    print(labels)
    four_buttons_template = [
        [{
            "action": {
                "type": "text",
                "payload": str(labels[0][0]),
                "label": labels[0][1]
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": str(labels[1][0]),
                "label": labels[1][1]
            },
            "color": "default"
        }],
        [{
            "action": {
                "type": "text",
                "payload": str(labels[2][0]),
                "label": labels[2][1]
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": str(labels[3][0]),
                "label": labels[3][1]
            },
            "color": "default"
        }]
    ]

    keyboard = {"one_time": one_time, "buttons": four_buttons_template}
    return json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def create_go_keyboard(one_time=True):
    one_button_template = [
        [{
            "action": {
                "type": "text",
                "payload": '{"test_button": "1"}',
                "label": "Поехали!"
            },
            "color": "positive"
        }
        ]
    ]
    keyboard = {"one_time": one_time, "buttons": one_button_template}
    return json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def create_start_keyboard(one_time=True):
    one_button_template = [
        [{
            "action": {
                "type": "text",
                "payload": '{"command":"start"}',
                "label": "Начать"
            },
            "color": "default"
        }
        ]
    ]
    keyboard = {"one_time": one_time, "buttons": one_button_template}
    return json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def create_next_block_need_keyboard(one_time=False):
    two_buttons_template = [
        [{
            "action": {
                "type": "text",
                "payload": '{"next_block_button": "1"}',
                "label": "Следующая задача"
            },
            "color": "default"
        },
        {
            "action": {
                "type": "text",
                "payload": '{"next_block_button": "2"}',
                "label": "На сегодня хватит"
            },
            "color": "default"
        }]
    ]

    keyboard = {"one_time": one_time, "buttons": two_buttons_template}
    return json.dumps(keyboard, ensure_ascii=False).encode('utf-8')


def create_answer(data, token, dialog):
    user_id = data['user_id']

    print('create_answer ', data)

    # Default values
    message, attachment, keyboard = 'Непонятно', '', None

    current_block = None

    try:
        if dialog.is_state_default():
            message = 'Привет! Ты только что нажал на кнопку старт! Давай решать задачи :)'
            dialog.change_state_to_need_next()
            keyboard = create_go_keyboard()

        elif dialog.is_state_need_next():
            try:
                current_block = ChoiceBlock.objects.get(pk=dialog.blocks_ids[dialog.current_block_pointer])
                message = str(current_block)
                current_options = current_block.get_options()
                keyboard = create_keyboard_for_block([(int(option.pk), str(option)) for option in current_options])
                dialog.change_state_to_need_answer()
            except Exception:
                message = 'Похоже, для вас больше нет задач на сегодня. Отдыхайте!'

        elif dialog.is_state_need_answer():
            current_block = ChoiceBlock.objects.get(pk=dialog.blocks_ids[dialog.current_block_pointer])

            current_result = ChoiceBlockResult.create(UserSocialAuth.objects.get(uid=str(user_id), provider='vk').user,
                                     current_block, [int(data["payload"])])
            current_result.set_score()
            if current_result.correct():
                message = 'Верно!'
            else:
                message = 'Неверно!'
            dialog.change_state_to_need_next()
            # TODO обрабатывать состояние, когда задачи закончились, уметь из него выходить
            update_result = dialog.update_pointer()
            # if update_result is not None:

            keyboard = create_next_block_need_keyboard()


        else:
            message = 'Произошло что-то странное'

        vkapi.send_message(user_id, token, message, attachment, keyboard)
        print('exit create answer')
    except Exception as e:
        print('create_answer exception', e)
        traceback.print_exc()


def create_dialog(user_id, token):
    print('handlers.py create_dialog')
    first_name, last_name = vkapi.get_vk_user_info(user_id, token)
    current_dialog = get_dialog(user_id, token)
    if current_dialog is None:
        try:
            current_dialog = Dialog.objects.create_dialog(user_id, first_name, last_name)
        except Exception as e:
            print('create_dialog exception', e)
            current_dialog = None
    return current_dialog


def get_dialog(user_id, token):
    print('handlers.py get_dialog')
    try:
        current_dialog = Dialog.objects.get(user=UserSocialAuth.objects.get(uid=str(user_id), provider='vk').user)
        return current_dialog
    except Exception as e:
        print('get_dialog exception', e)
        return None
