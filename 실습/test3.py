import requests
from pprint import pprint as print
API_URL = 'https://jsonplaceholder.typicode.com/users/'

user_list =[]
for i in range(1,11):
    response = requests.get(API_URL+str(i))
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dict_temp = {'name':parsed_data['name'],'lat':parsed_data['address']['geo']['lat'],'lng':parsed_data['address']['geo']['lng'],'company name':parsed_data['company']['name']}
        user_list.append(dict_temp)
print(user_list)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def create_user(user_list):
    censored_user_list = {}
    for user in user_list:
        if censorship(user):
            censored_user_list[user['company name']] = [user['name']]
    return censored_user_list

def censorship(user):
    if user['company name'] in black_list:
        print(f"{user['company name']} 소속의 {user['name']} 은/는 등록할 수 없습니다")
        return False
    else:
        print("이상 없습니다")
        return True

print(create_user(user_list))
# JSON -> dict 데이터 변환
# parsed_data = response.json()

# # 응답 데이터 출력
# print(response)

# # 변환 데이터 출력
# print(parsed_data)
# # 변환 데이터의 타입
# print(type(parsed_data))

# 특정 데이터 출력
# print(parsed_data['name'])

# print(parsed_data['username'])
# print(parsed_data['company']['name'])
