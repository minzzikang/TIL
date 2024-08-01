import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cnt = 0  # 정렬 횟수 확인
answer = -1

for i in range(N-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            cnt += 1
            A[j], A[j+1] = A[j+1], A[j]

            if cnt == K:
                answer = f'{A[j]} {A[j+1]}'

print(answer)