def backtracking(r, now_s):
    global min_v
    # 최적화
    if now_s >= min_v:  # 현재까지 구한 비용 합이 최솟값보다 클 경우 더 이상 구할 필요x
        return

    # 종료 조건
    if r == N:  # 모든 공장이 생산할 제품을 고름
        min_v = min(now_s, min_v)
        return

    for i in range(N):
        is_possible = True
        for j in range(N):
            if v[j][i] == 1:
                is_possible = False
                break
        if is_possible:
            v[r][i] = 1  # r행에 i번째 열을 고를 수 있다(제품 결정)
            # r+1행 결정하러
            # 현재까지 비용에 더해주기
            backtracking(r+1, now_s + expense[r][i])
            # 돌아오면 제품 결정 초기화
            v[r][i] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 제품 수
    expense = [list(map(int, input().split())) for _ in range(N)]

    # print(expense)
    min_v = 215
    v = [[0] * N for _ in range(N)]

    backtracking(0, 0)

    print(f'#{tc} {min_v}')