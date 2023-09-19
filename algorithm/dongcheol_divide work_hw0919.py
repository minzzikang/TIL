def dfs(r, now_v):
    global max_v
    # 최적화
    # 0이하 수라서 곱할수록 작아짐.
    # 현재까지 구한 확률이 최대 확률보다 작다면 더 이상 구할 필요 x
    if now_v <= max_v:
        return

    # 종료 조건
    if r == N:  # r행의 자리를 모두 정함(직원들 일 분배 끝)
        max_v = max(now_v, max_v)  # 최대값 갱신
        return

    # 재귀 호출
    for i in range(N):
        if visited[i] == 0:  # 아직 i번재 열 고르지 않았으면
            visited[i] = 1  # i번째 열의 자리가 정해졌음
            dfs(r+1, now_v * arr[r][i]*0.01)  # r+1행의 자리 구하러
            visited[i] = 0  # 초기화


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 일이 성공할 확률(직원 N * 일 N)
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)

    max_v = 0  # 일이 성공할 최대 확률(곱해줘야 함)
    visited = [0] * N

    dfs(0, 1)  # 확률 초기값은 1(곱해야 되서)
    print(f"#{tc} {format(max_v*100, '6f')}")