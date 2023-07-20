# # print 함수에 (end = " ") 넣으면 기본값인 줄바꿈이 아닌 띄어쓰기로 출력


# # 반복문에서의 else 구문
# # 반복문이 중간에 종료된 적 있는지 검사할 때 유용
# str_1 = 'apple'
# str_2 = 'banana'

# for i in str_2:
#     # apple 문자열을 순회하며 알파벳 b가 있으면 b! 출력 후 반복문 종료
#     if i == 'b':
#         print('b!')
#         break
# else:  # 반복문 실행 이후 실행 (break로 종료되지 않았을 경우)
#     print('이 단어 안에는 b가 없습니다.')


# 0~9 요소 가지는 리스트 생성

# 방법 2
new_li_2 = [i for i in range(10) if i % 2 == 1]
new_li_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# if-esle 구문은 앞으로 나옴 / 가독성 떨어져서 비추천
# elif는 사용 안됨, 중첩 조건은 가능
print(new_li_2)
print(new_li_3)

# # 리스트 생성법 비교
# # 정수 1,2,3 요소로 가지는 새로운 리스트 생성하기
# numbers = [1, 2, 3]
# # 1. for loop
# new_numbers = []
# for number in numbers:
#     new_numbers.append(int(number))
# print(new_numbers)

# # 2. map 활용
# new_numbers_2 = list(map(int, numbers))
# print(new_numbers_2)

# # 3. list comprehension
# new_numbers_3 = [int(number) for number in numbers]
# print(new_numbers_3)

# # pass는 코드 작성 중(함수 정의 시) 미완성 시 유용하게 사용 - 문법오류 막음

# # enumerate(iterable, ) - 인덱스와 값 함께 사용하기 위해 사용
# result = ['a', 'b', 'c']

# print(enumerate(result))
# print(list(enumerate(result)))  # 튜플이 packing 되어서 표현

# for index, elem in enumerate(result):
#     print(index, elem)

# # dict comprehension
# my_dict = {i: i**2 for i in range(10)}

# print(my_dict)

# # for 문으로 dict 반복
# scores = { 'minji' : 100, 'minsu' : 80, 'lisa' : 65}

# # 1. 기본적으로 key값만 가져오기 때문에 key 값으로 value값도 조회해서 가져와야 함
# for name in scores:
#     print(f'{name} : {scores[name]}')  # {scores.get(name)} 도 가능

# # 2. dict에서 key 값만 가져와서 사용
# for name in scores.keys():
#     print(f'{name} : {scores[name]}')

# # 3. dict에서 value 값만 가져와서 사용
# for score in scores.values():
#     print(score)

# # 4. key, value 모두 사용
# for key, value in scores.items():
#     print(f'{key} : {value}')