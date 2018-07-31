# Django core
import json
from . import handlers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# VK_GROUP_TOKEN = '67888d06aa888f4c9dc0a09cea3538dc0ec664967c08ed87a36613a82dcdddb174355b39172c7dfdf9bbb'
# TODO вынести константы в отдельный файл
VK_GROUP_TOKEN = 'f1449d43928c1580ff2997fbc95720ddca27cd084a65a38bac113e7fde3cbf5782391fd430548fb5984d0'
VK_GROUP_CONFIRMATION_TOKEN = 'bcc75ce1'
VK_GROUP_ID = 167796316



# Url, where user redirects after success vk authorization
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(':)', data)
        if 'type' not in data.keys():
            print('Data: {}'.format(data))
            return HttpResponse('not vk')
        # gropup settings, used to confirm server address
        if data['type'] == 'confirmation':
            return HttpResponse(VK_GROUP_CONFIRMATION_TOKEN)

        # user - bot conversation
        elif data['type'] == 'message_new':
            if 'payload' in data.keys():
                user_id = data['user_id']
                payload = data['payload']

                # Пользователь первый раз начал переписку с сообществом
                if payload == '{"command":"start"}':
                    # TODO заполнять данные, кроме id, например first_name, last_name
                    dialog = handlers.create_new_dialog(user_id, VK_GROUP_TOKEN)
                else:
                    # get dialog to user
                    dialog = handlers.get_dialog(user_id, VK_GROUP_TOKEN)

            else:
                user_id = data['object']['user_id']
                print(f'user_id: {user_id}')
                # код ниже, чтобы обработать свою кнопку Начать
                # потом можно будет выпилить
                if data['object']['payload'] == '{"command":"start"}':
                    # TODO заполнять данные, кроме id, например first_name, last_name
                    dialog = handlers.create_new_dialog(user_id, VK_GROUP_TOKEN)
                else:
                    dialog = handlers.get_dialog(user_id, VK_GROUP_TOKEN)

            handlers.create_answer(data['object'], VK_GROUP_TOKEN, dialog)
            return HttpResponse("ok")
    else:
        return HttpResponse('not post')


