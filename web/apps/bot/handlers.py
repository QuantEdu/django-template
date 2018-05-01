from . import vkapi


def create_answer(data, token):
    user_id = data['user_id']
    body = data['body'].lower()

    # Default values
    message, attachment = 'Непонятно', ''

    if body in ['help', 'помощь']:
        message = 'Привет, я новый бот! Ты выбрал команду help'
    if body in ['задача']:
        message = 'Привет, я новый бот! Ты выбрал команду help'
        attachment = 'photo-165396328_456239018'
    else:
        message = 'Привет, я новый бот! Я тебя не понял. Поэтому не шли мне больше {}'.format(body)
    vkapi.send_message(user_id, token, message, attachment)