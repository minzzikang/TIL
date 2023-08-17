T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 숫자 개수, M: 작업 횟수
    number = list(map(int, input().split()))

    Q = [0] * (M+1)
    front = rear = -1

    for i in range(N):
        rear += 1
        Q[rear] = number[i]

    for j in range(N, M+1):
    # 큐의 처음 원소를 맨 뒤로 저장하기
        front += 1
        temp = Q[front]
        rear += 1
        Q[rear] = temp

    print(f'#{tc} {Q[rear]}')