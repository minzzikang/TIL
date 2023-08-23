T = int(input())
for tc in range(1, T+1):
    goal = list(map(int, input()))  # 원래의 메모리 값
    N = len(goal)
    now = [0] * N  # 현재 메모리 값(0으로 초기화됨)

    cnt = 0  # 바꿔야 하는 횟수

    for i in range(N):
        # 원래 메모리와 현재 메모리의 같은 위치에 있는 값이 일치하지 않을 때
        if goal[i] != now[i]:
            cnt += 1  # 바꾸는 횟수 1 증가

            # 값이 같지 않으면 goal의 i번째 인덱스에 들어있는 값으로 변경
            # i번째부터 메모리의 끝까지 다 바꿔줘야 하므로 for문 사용
            for j in range(i, N):
                now[j] = goal[i]

    print(f'#{tc} {cnt}')