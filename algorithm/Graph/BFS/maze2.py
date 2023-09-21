import sys
sys.stdin = open('input.txt', 'r')

def bfs(sr, sc):
    visited = [[0] * 100 for _ in range(100)]
    Q = []

    # 미로 탐색 방향(상하좌우)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    # 시작지점 방문 표시
    Q.append((sr, sc))
    visited[sr][sc] = 1

    while Q:  # 큐가 빌 때 까지 반복
        r, c = Q.pop(0)

        if maze[r][c] == 3:
            return 1  # 도달 가능

        for d in range(4):
            # 다음 방향 탐색
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 방향이 갈 수 있는 길인지 확인
            if 0 <= nr < 100 and 0 <= nc < 100 and maze[nr][nc] != 1 and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = 1

    return 0  # 갈 수 있는 길 없음


T = 10
for tc in range(1, T+1):
    int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    print(f'#{tc} {bfs(1,1)}')