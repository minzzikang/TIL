# 괄호
T = int(input())

for tc in range(T):
    check = input()
    stack = []

    for i in check:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                print('NO')
                break
            else:
                stack.pop()

    else:
        if stack:
            print('NO')
        else:
            print('YES')