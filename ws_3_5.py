# 실습 번호.py
import ws_3_2, book

number_of_people = 0

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(ws_3_2.create_user, name, age, address))
print(many_user)

# def user_lambda(user):
#     return {'name': user['name'], 'age': age['age']}

user_info_list = list(
    map(lambda user : {'name': user['name'], 'age': user['age']}, many_user)
)

print(user_info_list)

def rental_book(info):
    n = info['age'] // 10  # 변수 n에 dict 'info'에서 'age' 를 key로 가진 value값에서 10으로 나눈 값 할당
    book.decrease_book(n)
    print(f"{info['name']}님이 {n}권의 책을 대여하였습니다.")

result = list(map(rental_book, user_info_list))