from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


T = int(input())
for tc in range(1, T+1):
    # N*M 지도
    N, M = map(int, input().split())
    Q = deque()  # 물 정보 담는 큐

    # 한번에 입력받지 않고 입력 받으면서 w 넣기
    pool = [[-1] * M for _ in range(N)]

    for r in range(N):
        row = list(input())  # 한 줄씩 입력받기
        for c in range(M):
            if row[c] == 'W':
                Q.append((r,c))
                pool[r][c] = 0  # 물이 있는 곳의 거리는 0

    sum_distance = 0  # 이동 거리 합

    while Q:
        r, c = Q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 배열 범위 안에 있고 물이 있는 곳이 아니라면
            if 0 <= nr < N and 0 <= nc < N and pool[nr][nc] == -1:
                Q.append((nr, nc))
                pool[nr][nc] = pool[r][c] + 1
                sum_distance += pool[nr][nc]



