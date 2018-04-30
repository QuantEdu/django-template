from . import vkapi
import importlib, os
from . import commands


def get_answer(body):
   message = 'Привет, я новый бот! Не шли мне больше {}'.format(body)
   return message

def get_answer(body):
    # Сообщение по умолчанию если распознать не удастся
    message = "Прости, не понимаю тебя. Напиши 'помощь', чтобы узнать мои команды"
    attachment = ''
    print(commands.command_list)
    for c in commands.command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment

def create_answer(data, token):
   from .commands import hello, info
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message, attachment)