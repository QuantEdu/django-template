# Django core
import json
import vk
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

VK_GROUP_TOKEN = '67888d06aa888f4c9dc0a09cea3538dc0ec664967c08ed87a36613a82dcdddb174355b39172c7dfdf9bbb'

# Url, where user redirects after success vk authorization
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if 'type' not in data.keys():
            return 'not vk'
        if data['type'] == 'confirmation':
            return HttpResponse('b609300d')
        elif data['type'] == 'message_new':
            session = vk.Session()
            api = vk.API(session, v=5.0)
            user_id = data['object']['user_id']
            api.messages.send(access_token=VK_GROUP_TOKEN, user_id=str(user_id), message='Привет, я новый бот! Не шли мне больше {}'.format(data['object']['body']))
            return HttpResponse('ok')
        else:
            print('Data: {}'.format(data))

    else:
        return HttpResponse('not post')