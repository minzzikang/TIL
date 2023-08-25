def omok(N, board):
    # 오목 살펴 볼 방향(12시부터 4방향)
    dr = [-1, -1, 0, 1]
    dc = [0, 1, 1, 1]

    for r in range(N):
        for c in range(N):
            # 돌이 놓여있지 않는 곳은 건너 뛰기
            if board[r][c] == '.':
                continue

            # 돌이 놓인 기준점일 경우에 방향 탐색하기
            for d in range(4):  # 4방향 탐색
                for k in range(1, 4+1):  # 기준점 제외 4칸만 확인하면 됌
                    # 다음에 탐색해 볼 방향
                    nr = r + dr[d] * k
                    nc = c + dc[d] * k

                    # 그 방향이 유효한지 확인
                    # 유효하지 않다면 중지
                    if not ((0 <= nr < N and 0 <= nc < N) and (board[nr][nc] == 'o')):
                        break

                else:  # break문에 걸리지 않았다 = 기준점에서 4칸까지 갔을때의 탐색을 마침 = 오목 찾음
                    return 'YES'

    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 오목판 크기
    board = [list(input()) for _ in range(N)]

    ans = omok(N, board)
    print(f'#{tc} {ans}')
