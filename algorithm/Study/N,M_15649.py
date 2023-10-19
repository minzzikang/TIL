def dfs(n, lst):  # n: 고른 숫자 개수, lst: 고른 숫자로 만든 수열
    # 종료 조건
    if n == M:
        ans.append(lst)
        return

    # 재귀 호출
    for i in range(1, N+1):  # 숫자는 1부터 있으므로 0번 인덱스 사용x
        if visited[i] == 0:
            visited[i] = 1
            dfs(n+1, lst+[i])
            visited[i] = 0  # 초기화


N, M = map(int, input().split())
visited = [0] * (N+1)  # 숫자 0은 쓰지 않으므로
ans = []  # 조건에 맞는 수열을 담을 리스트

dfs(0, [])

for i in ans:
    print(*i)

