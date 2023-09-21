from heapq import heappush, heappop

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dijkstar():
    pq = []
    # 좌측 상단 시작의 위치는 0,0
    heappush(pq, (0, 0, 0))  # 출발점 초기화 (가중치, r,c)
    fuel[0][0] = 0  # 출발지에서 출발지까지 갈때 드는 연료는 0

    while pq:
        w, r, c = heappop(pq)

        if fuel[r][c] < w:
            continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                h_diff = 0
                if arr[r][c] < arr[nr][nc]:
                    h_diff = arr[nr][nc] - arr[r][c]

                # nr, nc까지 이동하는데 사용한 연료량 = r,c까지 이동하는데 사용한 연료량 + 기본 사용량(1) + 높이 차
                cost = fuel[r][c] + h_diff + 1

                # 이전에 구한 연료량(nr,nc)보다 작을때 갱신
                if cost < fuel[nr][nc]:
                    fuel[nr][nc] = cost
                    heappush(pq, (cost, nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # N*N
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(height)

    fuel = [[9999999] * N for _ in range(N)]  # 값이 (r,c) 들어가야 하므로

    dijkstar()
    print(f'#{tc} {fuel[N-1][N-1]}')