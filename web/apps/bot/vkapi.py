import vk

session = vk.Session()
api = vk.API(session, v=5.78)


def send_message(user_id, token, message, attachment, keyboard):
    print('vkapi.py send_message')
    try:
        if keyboard is None:
            api.messages.send(access_token=token, user_id=str(user_id),
                    message=message, attachment=attachment)
        else:
            api.messages.send(access_token=token, user_id=str(user_id),
                    message=message, attachment=attachment, keyboard=keyboard)
    except Exception as e:
        print(e)


def get_vk_user_info(user_id, token):
    print(f'vkapi.py get_vk_user_id by {user_id}')
    api.users.get(access_token=token, user_ids=user_id, fields="photo_50, city, verified")