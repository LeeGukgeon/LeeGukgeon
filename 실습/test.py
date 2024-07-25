number_of_people = 0
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']
number_of_book = 100

def create_user(name=None,age=None,address=None):
    user_info = {'name':name,'age':age,'address':address}
    return user_info

many_user = list(map(create_user, name, age, address))
print(many_user)

def add_user(name=None,age=None,address=None):
    global many_user
    many_user.append({'name':name,'age':age,'address':address})
    return 0

add_user('뭐',25,'서울')

info = list(map(lambda x: {'name': x['name'],'age' :x['age']},many_user))
print(info)

def rental_book(info):

    decrease_book(info['age']%10)
    name = info['name']
    age = info['age']%10
    print(f'{name}님이 {age}권의 책을 대여하였습니다.')
    return 0


def decrease_book(rentnum):
    global number_of_book
    number_of_book -= rentnum
    print(f'남은 책의 수 : {number_of_book}')

list(map(rental_book,many_user))

# new_user=list(map(lambda x: {'name': x['name'],'age' :x['age']}, [create_user('국',26,'광주')]))
# list(map(rental_book,new_user))
