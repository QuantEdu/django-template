# Django core


def vk_complete(request):

    if request.method == 'GET':
        uid = request.GET.get('uid', '')
        first_name = request.GET.get('first_name', '')
        last_name = request.GET.get('last_name', '')
        photo = request.GET.get('photo', '')
        photo_rec = request.GET.get('photo_rec', '')
        hash = request.GET.get('hash', '')
        # if user already exist - check authorization hash and authorize in django
        # if user not exist - create a new one and take to user creation form
        print(uid)
        return True
