# 실습 번호.py
import book

number_of_people = 0
user_list = []

def increase_user():
    global number_of_people
    number_of_people += 1

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    print(f'{name}님 환영합니다!')

    return user_info

many_user = list(map(create_user, name, age, address))
print(many_user)

def user_lambda(user):
    return {'name': user['name'], 'age': age['age']}

user_info_list = list(
    map(lambda user : {'name': user['name'], 'age': user['age']}, many_user)
)

print(user_info_list)

def rental_book(info):
    n = info['age'] // 10
    book.decrease_book(n)
    print(f"{info['name']}님이 {n}권의 책을 대여하였습니다.")

result = list(map(rental_book, user_info_list))