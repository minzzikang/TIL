import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    mission = sys.stdin.readline().split()
    if mission[0] == 'push':
        stack.append(mission[1])

    if mission[0] == 'pop':
        if stack:
            stack.pop()
            top -= 1
        else:
            print(-1)
    if mission[0] == 't':
        print(stack[top])
    if mission[0] == 's':
        print(len(stack))
    if mission[0] == 'e':
        if stack:
            print(0)
        else:
            print(1)