<<<<<<< HEAD
from collections import deque

# 나이트 이동방향
dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

def bfs():
    Q = deque()
    Q.append((sr, sc))

    while Q:
        r, c = Q.popleft()
        if r == er and c == ec:
            return visited[r][c] - 1

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    I = int(input())  # 체스판 한 변의 길이
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    visited[sr][sc] = 1  # 시작점 방문 표시

    print(bfs())
=======
from collections import deque

# 나이트 이동방향
dr = [-2,-1,1,2,2,1,-1,-2]
dc = [1,2,2,1,-1,-2,-2,-1]

def bfs():
    Q = deque()
    Q.append((sr, sc))

    while Q:
        r, c = Q.popleft()
        if r == er and c == ec:
            return visited[r][c] - 1

        for d in range(8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    I = int(input())  # 체스판 한 변의 길이
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    visited = [[0] * I for _ in range(I)]
    visited[sr][sc] = 1  # 시작점 방문 표시

    print(bfs())
>>>>>>> 34e6b8153a4a3105096c54620c8c7c9ec126a759
