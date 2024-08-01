N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0  # 정렬 횟수 확인

for i in range(N-1, 0, -1):
    for j in range(i):
        if A[j] > A[j+1]:
            cnt += 1
            A[j], A[j+1] = A[j+1], A[j]

            if cnt == K:
                print(*A)
                exit()

print(-1)