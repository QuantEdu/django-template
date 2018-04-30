# Django core
import json
from django.http import HttpResponse


# Url, where user redirects after success vk authorization
def callback(request):
    if request.method == 'POST':
        data = json.loads(request.data)
        print(data)
        print(request)
        if 'type' not in data.keys():
            return 'not vk'
        if data['type'] == 'confirmation':
            return 'b609300d'
        else:
            return HttpResponse('ok')
    else:
        return HttpResponse('not post')