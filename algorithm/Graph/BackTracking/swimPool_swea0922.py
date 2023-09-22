def dfs(month, sum_cost):
    global min_cost

    # 가지치기
    # 현재까지 구한 비용이 최소값 넘는 경우
    if sum_cost > min_cost:
        return

    # 종료 조건
    if month > 12:  # 1년 끝
        min_cost = min(min_cost, sum_cost)
        return

    # 재귀 호출
    # 1일권만 사용
    dfs(month+1, sum_cost + (plans[month] * d_cost))

    # 1달권만 사용
    dfs(month+1, sum_cost + m_cost)

    # 3달권만 사용
    dfs(month+3, sum_cost + ms_cost)

    # 1년권 사용
    dfs(month+12, sum_cost + y_cost)



T = int(input())
for tc in range(1, T+1):
    d_cost, m_cost, ms_cost, y_cost = map(int, input().split())
    # 1월부터 이므로 0번 인덱스 자리 추가
    plans = [0] + list(map(int, input().split()))

    min_cost = int(1e9)  # 가장 적은 비용

    dfs(1, 0)
    print(f'#{tc} {min_cost}')