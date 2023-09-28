from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
# print(miro)

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r, c):
    q = deque()
    q.append((r,c))

    while q:
        r,c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and miro[nr][nc] == 1:
                q.append((nr, nc))
                miro[nr][nc] = miro[r][c] + 1

    return miro[N-1][M-1]

print(bfs(0,0))