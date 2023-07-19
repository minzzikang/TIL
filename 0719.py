numbers = [1, 2, 3]
result = map(str, numbers)

print(result)
print(list(result))

result = []
for number in numbers:
    result.append(str(number))

print(result)

# packing
nums = 1, 2, 3, 4, 5
a, *b, c = nums
print(a, b, c)
print(*nums)  # 리스트 요소 unpacking / print(nums[0], nums[1], ...)

# print 원래 함수로 복구
print = __builtins__.print


# filter(function, iterable)
# function의 결과는 T or F (T 인것만 골라서 반환)
# list의 홀수만 걸러내는 함수
def odd(n):
    return n % 2  # 2로 나눈 나머지가 1(T)인 경우에만 반환

numbers2 = [1, 2, 3, 4, 5]
new_numbers = list(filter(odd, numbers2))  #list(filter(lambda n: n % 2, numbers2))도 같은 기능

print(new_numbers)
