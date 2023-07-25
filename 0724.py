# # 리스트 탐색/정렬 메서드
dic = {'c' : 3, 'b' : 10, 'a' : 5}
# ex) dict 정렬할 때 키가 아닌 값 기준으로 정렬하고 싶을 때
# def sort_key(item):
#     print(item)
#     return item[1]  # 튜플에서 value 값은 인덱스 1 값을 가지므로

# sort_key(dic)

print(sorted(dic, key=lambda item: item[1]))
# # key 인자는 정렬 방법 서술할 함수(lambda도 자주 쓰임)
print(dic.items(), key=lambda item: item[1])
# items 함수는 dic의 key-value 값을 튜플로 바꿈