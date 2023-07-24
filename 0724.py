# # 문자열 조회/탐색 및 검증 메서드 (공식문서에서 모든 메서드 확인 가능)

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