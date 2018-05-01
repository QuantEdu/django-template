from . import vkapi


def create_answer(data, token):
   user_id = data['user_id']
   body = data['body'].lower()
   if body in ['help', 'помощь']:
       message = 'Привет, я новый бот! Ты выбрал команду help'
   else:
       message = 'Привет, я новый бот! Я тебя не понял. Поэтому не шли мне больше {}'.format(body)
   vkapi.send_message(user_id, token, message)