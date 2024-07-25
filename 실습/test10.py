# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}

    def get_user_info(self):
        self.user_data['name'] = input('이름을 입력하세요 :')
        self.user_data['age'] = int(input('나이를 입력하세요 :'))
        
    def display_user_info(self):
        print('사용자 정보 : ')
        print(f'이름 : {self.user_data["name"]}')
        print(f'나이 : {self.user_data["age"]}')

user = UserInfo()


try:
    user.get_user_info()
    print(user.user_data)
except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
            print('사용자 정보가 입력되지 않았습니다.')
except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')
if user.user_data['name']=='':
    print('사용자 정보가 입력되지 않았습니다.')
else:
    user.display_user_info()

