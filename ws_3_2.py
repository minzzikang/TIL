number_of_people = 0

def increase_user():
    global number_of_people  # immutable data 수정할 때 global 사용
    number_of_people += 1

def create_user(name, age, address):
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    increase_user()
    print(f'{name}님 환영합니다!')
    return user_info

print(f'현재 가입 된 유저 수 : {number_of_people}')
print(create_user('홍길동', 30, '서울'))
print(f'현재 가입 된 유저 수 : {number_of_people}')