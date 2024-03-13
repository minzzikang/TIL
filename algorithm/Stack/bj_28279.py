import sys
from collections import deque

N = int(input())
numbers = deque()

for _ in range(N):
    num = list(map(int, sys.stdin.readline().strip().split()))
    if num[0] == 6:
        if len(numbers) != 0:
            print(0)
        else:
            print(1)

    if num[0] == 1:
        numbers.appendleft(num[1])

    if num[0] == 2:
        numbers.append(num[1])

    if num[0] == 3:
        if len(numbers) != 0:
            print(numbers.popleft())
        else:
            print(-1)

    if num[0] == 4:
        if len(numbers) != 0:
            print(numbers.pop())
        else:
            print(-1)

    if num[0] == 5:
        print(len(numbers))

    if num[0] == 7:
        if len(numbers) != 0:
            print(numbers[0])
        else:
            print(-1)

    if num[0] == 8:
        if len(numbers) != 0:
            print(numbers[-1])
        else:
            print(-1)