black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    for user in user_list:
        if censorship(user):
            censored_user_list = {user['company']['name']:[user['name']]} 
    return censored_user_list

def censorship(user):
    if user['company']['name'] in black_list:
        print(f"{user['company']['name']} 소속의 {user['name']} 은/는 등록할 수 없습니다")
        return False
    else:
        print("이상 없습니다")
        return True

create_user()