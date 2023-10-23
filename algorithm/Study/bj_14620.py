<<<<<<< HEAD
# 기준점, 상, 하, 좌, 우 방향
dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

def check(r, c):
    for dr, dc in dir:
        nr = r + dr
        nc = c + dc
        if not ((0 <= nr < N) and (0 <= nc < N)) or visited[nr][nc]:
            return False
    return True


def dfs(cost, cnt):  # cnt: 꽃 개수
    global ans

    # 종료조건
    if cnt == 3:
        ans = min(ans, cost)

    # 재귀 호출
    for r in range(1, N-1):
        for c in range(1, N-1):
            if check(r,c):
                visited[r][c] = 1
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    visited[nr][nc] = 1
                    cost += ground[nr][nc]
                dfs(cost, cnt+1)
                # 회귀해서 다시 방문 안했다고 표시
                visited[r][c] = 0
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    visited[nr][nc] = 0


N = int(input())  # 화단 한 변 길이
ground = [list(map(int, input().split())) for _ in range(N)]  # 각 땅의 가격
visited = [[0] * N for _ in range(N)]
ans = int(1e9)


dfs(0, 0)
=======
# 기준점, 상, 하, 좌, 우 방향
dir = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]

def check(r, c):
    for dr, dc in dir:
        nr = r + dr
        nc = c + dc
        if not ((0 <= nr < N) and (0 <= nc < N)) or visited[nr][nc]:
            return False
    return True


def dfs(cost, cnt):  # cnt: 꽃 개수
    global ans

    # 종료조건
    if cnt == 3:
        ans = min(ans, cost)

    # 재귀 호출
    for r in range(1, N-1):
        for c in range(1, N-1):
            if check(r,c):
                visited[r][c] = 1
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    visited[nr][nc] = 1
                    cost += ground[nr][nc]
                dfs(cost, cnt+1)
                # 회귀해서 다시 방문 안했다고 표시
                visited[r][c] = 0
                for dr, dc in dir:
                    nr = r + dr
                    nc = c + dc
                    visited[nr][nc] = 0


N = int(input())  # 화단 한 변 길이
ground = [list(map(int, input().split())) for _ in range(N)]  # 각 땅의 가격
visited = [[0] * N for _ in range(N)]
ans = int(1e9)


dfs(0, 0)
>>>>>>> 34e6b8153a4a3105096c54620c8c7c9ec126a759
print(ans)