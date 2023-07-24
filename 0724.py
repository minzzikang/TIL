# '''
# 메서드: 객체에 속한 함수 (객체 상태 조작/동작 수행)
# 일반 함수와 존재하고 있는 위치가 다름
# 클래스(파이썬에서 타입을 표현하는 방법) 내부에 정의되는 함수
# ex) append : 리스트에 속해 있는 메서드
# '''
# # print(help(list))

# # 메서드 호출법 (문자열 메서드 예시)
# print('hello'.capitalize())   # Hello,  원본이 아닌 복사본


# # 시퀀스 데이터 구조
# # 문자열 조회/탐색 및 검증 메서드 (공식문서에서 모든 메서드 확인 가능)
# # 문자열은 변경 불가능해서 메서드 사용시 항상 새문자열(복사본) 반환
# # 메서드끼리 이어서 사용 가능 (앞의 메서드 결과에 대해 메서드 적용)
# print('banana'.find('a'))  # a의 첫 번째 위치 반환. 없으면 -1 반환
# # print('banana'.index('z'))  # a의 첫 번째 위치 반환. 없으면 오류 발생 (ValueError)

# string1 = 'HELLO world'
# string2 = 'Hello'
# string3 = 'hel354'
# print(string1.isupper())  # 전부 대문자로 이루어졌는지
# print(string2.islower())  # 전부 소문자로 이루어졌는지
# print(string3.isalpha())  # 문자열이 알파벳으로 이루어졌는지
# print(string1.title())  # 단어 시작만 대문자, 나머지는 소문자로 변경
# print(string1.swapcase())  # 대문자와 소문자 서로 변경

# # 파이썬 문법은 아니지만, 뒤의 []부분은 선택인자로 정해놓음(ebnf 표기법)
# # .replace(old, new[,count]) 바꿀 대상 글자를 새 글자로 바꿔 반환, count는
# text = 'Hello, world!'
# new_text = text.replace('world', 'Python')  # world 부분을 Python으로 교체
# print(new_text)  # Hello, Python!

# text2 = '  Hello, world!  '
# new_text2 = text2.strip()
# print(new_text2)  # 문자열 시작,끝 공백 (또는 지정문자 [char]) 제거)

# # 'separator'.join([iterable])
# words = ['Hello', 'world']
# text3 = '-'.join(words)  # iterable 요소들을 구분자로 하나의 문자열로 연결
# print(text3)


# # 리스트 값 추가/삭제 메서드
# my_list = [1, 2, 3]
# my_list2 = [4, 5, ,6]
# print(my_list.append(my_list2))  # None / 원본을 바꿨다는 얘기
# print(my_list.extend(my_list2))  # None / 원본을 바꿨다는 얘기

# my_list.append(my_list2)
# print(my_list)  # [1, 2, 3, [4, 5, 6]]

# my_list.extend(my_list2)
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# # .insert(i, x) 리스트에서 지정한 인덱스 i 위치에 항목 x를 삽입
# # .remove(x) 리스트에서 첫 번재로 일치하는 항목 삭제
# # .clear()  리시트 모든 항목 삭제
# # .pop(i) 리스트에서 지정한 인덱스 항목 제거 후 반환, 작성하지 않을 경우 마지막 항목 제거 후 반환
# item1 = my_list.pop()
# item2 = my_list.pop(0)

# print(item1)  # 5
# print(item2)  # 1
# print(my_list)  # [2, 3, 4]


# # 리스트 탐색/정렬 메서드
# # .index()  리스트에서 첫 번째로 일치하는 항목의 인덱스를 반환
# my_li = [1, 2, 3]
# index = my_li.index(2)
# print(index)  # 1

# .count(x)  리스트에서 항목 x가 등장하는 횟수 반환
# .sort()  원본 리스트를 오름차순으로 정렬 (복사본 x)
# my_li = [3, 1, 2]
# my_li.sort()  # 기본 오름차순(기본인자 reverse=False)
# print(my_li)  # [1, 2, 3]   내림차순 하려면 .sort(reverse=True)
# print(my_li.sort())  # 원복 복사하는거라서 결과값 None 나옴

# # sorted 함수(내장) - 알파벳, 한글 다 가능
# print(sorted(my_li))  # 원본 바꾸지 않고 정렬한 복사본을 반환
tup = (3, 4, 5, 6, 2)

print(sorted(tup))  # 리스트로 변경되서 정렬 값 반환
print(tup)

dic = {'c' : 3, 'b' : 10, 'a' : 5}
print(sorted(dic))  # key 값만 정렬  ['a', 'b', 'c']

# ex) dict 정렬할 때 키가 아닌 값 기준으로 정렬하고 싶을 때
def sort_key(item):
    print(item)
    return item[1]  # 튜플에서 value 값은 인덱스 1 값을 가지므로

print(sorted(dic.items(), key=sort_key))  # key 인자는 정렬 방법 서술할 함수(lambda도 자주 쓰임)
# (dic.items(), key=lambda item: item[1])
# items 함수는 dic의 key-value 값을 튜플로 바꿈


# .reverse() 리스트 순서를 역순으로 변경(단순 변경으로 정렬은 아님!)

numbers = [1, 2, 3]
# 1. 할당
list1 = numbers  # 같은 주소값 참조

# 2. 슬라이싱
list2 = numbers[:]  # 겉보기엔 같으나 슬라이싱은 값을 복사해 사용하기 때문에 다른 주소값

numbers[0] = 100
print(list1)  # [100, 2, 3]
print(list2)  # [1, 2, 3]