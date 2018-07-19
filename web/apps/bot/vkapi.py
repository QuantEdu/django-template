import vk

session = vk.Session()
api = vk.API(session, v=5.78)


def send_message(user_id, token, message, attachment, keyboard):
    print('vkapi.py send_message')
    try:
        if keyboard is None:
            result = api.messages.send(access_token=token, user_id=str(user_id),
                      message=message, attachment=attachment)
            print(result)
    except Exception as e:
        print(e)

