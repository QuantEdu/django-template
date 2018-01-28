# -*- coding: utf-8 -*-

# Настройки
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json, logging

TELEGRAM_TOKEN = '467191582:AAE7pMpdGsPULVRFyhf7Vk3kYwv8VeXfV4k'
DIALOG_FLOW_TOKEN = '281dbfa163e343fdba0368f4857c84d4'

# The Updater class continuously fetches new updates from telegram
updater = Updater(token='467191582:AAE7pMpdGsPULVRFyhf7Vk3kYwv8VeXfV4k')
dispatcher = updater.dispatcher

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# Обработка команд
def start_command(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text='Привет, {}, давай пообщаемся? Чтобы сломать мне мозг, напиши свою фамилию'.format(update.message.from_user))


# def text_message(bot, update):
#     response = 'Получил Ваше сообщение: ' + update.message.text
#     bot.send_message(chat_id=update.message.chat_id, text=response)


def text_message(bot, update):
    if update.message.text == 'Пирожок' or update.message.text == 'Пaрамонова':
        bot.send_message(chat_id=update.message.chat_id, text='Ути сладенькая! Грррря')
    else:
        request = apiai.ApiAI(DIALOG_FLOW_TOKEN).text_request()
        request.lang = 'ru'
        # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.session_id = 'BatlabAIBot'
        request.query = update.message.text
        response_json = json.loads(request.getresponse().read().decode('utf-8'))
        response = response_json['result']['fulfillment']['speech']
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


# Хендлеры
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)

# Добавляем хендлеры в диспетчер
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

# Начинаем поиск обновлений
updater.start_polling(clean=True)

# Останавливаем бота, если были нажаты Ctrl + C
updater.idle()
