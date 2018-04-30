# Django core
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Url, where user redirects after success vk authorization
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        data = request.body
        # print(data)
        print('Request: {}'.format(data))
        # if 'type' not in data.keys():
        #     return 'not vk'
        # if data['type'] == 'confirmation':
        #     return 'b609300d'
        # else:
        #     return HttpResponse('ok')
    else:
        return HttpResponse('not post')