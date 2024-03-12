N = int(input())
numbers = []

for _ in range(N):
    num = int(input())
    numbers.append(num)

# print(numbers)

for i in range(len(numbers)):
    min_n = min(numbers)
    print(min_n)
    numbers.remove(min_n)
