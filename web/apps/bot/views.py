# Django core
from django.http import HttpResponse


# Url, where user redirects after success vk authorization
def callback(request):
    print(request.body)
    return HttpResponse('ok')