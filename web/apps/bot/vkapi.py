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
    answer = api.users.get(access_token=token, user_ids=user_id)[0]
    print(answer)
    first_name = answer['first_name'].decode('utf-8')
    last_name = answer['last_name'].decode('utf-8')
    print(first_name, last_name)
    return first_name, last_name
