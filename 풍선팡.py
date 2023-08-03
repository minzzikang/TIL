T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    # 기준값으로부터 상하좌우 이동할 좌표값
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 최대 꽃가루 합
    max_flower = 0

    for r in range(N):
        for c in range(M):
            now_flower = A[r][c]
            # 기준 좌표에 들어있는 꽃가루 수만큼 추가로 더 터짐
            for p in range(1, A[r][c]+1):
                # 상하좌우로 반복하면서 꽃가루 합 구함
                for d in range(4):
                    nr = r + dr[d] * p
                    nc = c + dc[d] * p

                    if 0 <= nr < N and 0 <= nc < M:
                        now_flower += A[nr][nc]
            
            if max_flower < now_flower:
                max_flower = now_flower

    print(f'#{tc} {max_flower}')