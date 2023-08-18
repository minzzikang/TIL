def bfs(sr,sc):
    # 미로 탐색 방향: 상하좌우
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    visited = [[0] * N for _ in range(N)]
    Q = []

    # 시작행,시작열 방문 처리
    Q.append((sr, sc))
    visited[sr][sc] = 1

    while Q:
        r, c = Q.pop(0)

        if maze[r][c] == 3:  # 도착점일 경우
            return visited[r][c] - 2  # 거리 지나온 값에서 시작값과 끝값 2개 빼기

        for d in range(4):
            # 다음 방향 탐색
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 방향이 갈 수 있는 곳이라면
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and not visited[nr][nc]:
                Q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    return 0  # 도착점에 못 가는 경우

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작 위치 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr, sc = r, c

    print(f'#{tc} {bfs(sr, sc)}')