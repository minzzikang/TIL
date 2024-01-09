# 양치기 꿍
from collections import deque
def counting(r, c):
    sheep, wolf = 0, 0  # 초기 양,늑대 수
    q.append([r, c])
    visited[r][c] = 1  # 시작점 방문 처리

    while q:
        r, c = q.popleft()

        if data[r][c] == 'v':  # 늑대인 경우
            wolf += 1

        if data[r][c] == 'k':  # 양인 경우
            sheep += 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and data[nr][nc] != '#' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                q.append([nr, nc])

        if wolf >= sheep:
            sheep = 0  # 잡아 먹힘
        else:
            wolf = 0
        return sheep, wolf


R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# 상하좌우
dr = [-1,1,0,0]
dc = [0,0,-1,1]
q = deque()

ans_sheep, ans_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if data[i][j] != '#' and not visited[i][j]:
           counting(i,j)

print(ans_sheep, ans_wolf)