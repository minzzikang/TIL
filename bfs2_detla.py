dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 인덱스 유효 판단 함수
def is_valid(r,c):
    return 0 <= r < n and 0 <= c < n

# 이차원 배열 탐색 함수
# sr: 시작행, sc: 시작열
def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]

    Q = []
    Q.append((sr,sc))
    visited[sr][sc] = 1

    distance = 0  # 탈출하는데 몇 칸 이동했는지(최소 거리)

    while Q:  # 큐가 빌 때까지 탐색
        # 현재 단계에서 큐 안에 몇 개 까지만 확인하면 될지
        size = len(Q)

        for _ in range(size):
            r, c = Q.pop(0)  # 현재 방문하는 위치 r,c

            # 현재 방문 위치가 도착점인 경우 반복 중단
            if maze[r][c] == 99:
                print(f'탈출: {distance}')
                break

            # 현재 위치 r,c에서 4방향 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                    Q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

        distance += 1

    return distance

n = 7
maze = [[0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,0,1,0,1,0],
        [0,0,0,1,0,0,0],
        [1,0,1,1,1,0,1],
        [1,0,1,99,0,0,1],
        [0,0,1,1,1,0,1],
        ]

bfs(0,0)