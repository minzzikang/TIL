dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_water(arr, N, M):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                Q.append((i,j))
    return Q

def bfs(arr, N, M):
    visited = [[0] * M for _ in range(N)]

    while Q:
        sr, sc = Q.pop(0)

        for d in range(4):
            nr = sr + dr[d]
            nc = sc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 'W' and not visited[nr][nc]:
                visited[nr][nc] = visited[sr][sc] + 1

    return visited


T = int(input())
for tc in range(1, T+1):
    # N*M 지도
    N, M = map(int, input().split())
    map = [list(input()) for _ in range(N)]
    # print(map)
    min_v = 1000000
    Q = []

    print(find_water(map, N, M))
    print(bfs(map, N, M))



    # print(f'#{tc} {min_v}')
