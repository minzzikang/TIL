# 스택2
import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    com = input().rstrip()

    if len(com) > 2:  # 1이라서 append할 경우 (띄어쓰기 포함)
        stack.append(int(com[2:]))

    elif com == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif com == '3':
        print(len(stack))

    elif com == '4':
        if stack:
            print(0)
        else:
            print(1)

    elif com == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)