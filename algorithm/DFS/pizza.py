import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 화덕크기, M: 피자개수
    Ci = list(map(int, input().split()))  # 각 피자에 뿌려진 치즈 양

    # 다음에 꺼내올 피자 인덱스
    next_i = 0

    # 화덕을 큐로 만들기
    Q = [0] * 1000

    ofront = orear = -1

    # 화덕의 크기 만큼 피자 넣기
    for i in range(N):
        orear += 1
        # 나중에 꺼낼 때를 위해서 피자 번호도 같이 넣기
        Q[orear] = [i, Ci[i]]  # i번째 피자와 그 피자의 치즈 정보
        next_i += 1

    # 오븐에 남아 있는 피자 개수
    remain = N
    # 마지막에 꺼낸 피자의 번호
    last_idx = -1

    # 모든 피자의 치즈가 녹을때까지 반복
    while True:
        # 피자를 하나 꺼내서
        # 치즈를 녹이고 c // 2
        ofront += 1
        pizza_idx, pizza = Q[ofront]
        pizza //= 2

        # 남은 치즈 양이 0이 아니면 다시 오븐에 넣기
        if pizza != 0:
            orear += 1
            Q[orear] = [pizza_idx, pizza]

        # 남은 치즈 양이 0이면
        else:
            # 현재 오븐의 자리에 남은 피자를 하나 꺼내서 넣기
            if next_i < M:
                orear += 1
                Q[orear] = [next_i, Ci[next_i]]
                next_i += 1

            # 넣을 피자가 없으면? (next_i가 인덱스M을 벗어남)
            else:
                remain -= 1  # 오븐에서 피자 하나 뺌
                # 오븐에 남은 피자도 없는 상황이면 => 현재 피자의 번호가 정답
                if remain == 0:
                    last_idx = pizza_idx
                    break
    print(f'#{tc} {last_idx+1}')


