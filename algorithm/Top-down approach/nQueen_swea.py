def backtracking(r, remain):  # remain: 앞으로 놔야 하는 남은 퀸 갯수
    global cnt
    # 종료 조건
    if r == N and remain == 0:  # 모든 행의 퀸 자리를 결정함(퀸을 모두 놓았음)
        cnt += 1
        return

    # 재귀 호출
    # 현재 r 행에서 i번째 열에 퀸 놓을 수 있으면 놓고 r+1행에 퀸 놓으러 가기
    for i in range(N):
        # i번째 열에 퀸을 놓을 수 있나?
        is_place = True

        # 세로 방향에 퀸이 있는지 검사
        for j in range(r):  # r+1에는 아직 놓지 않아서 검사할 필요 없음(검사할 퀸이 없음)
            if board[j][i] == 1:
                is_place = False
                break

        # 대각선 방향에 퀸이 있는지 검사
        for j in range(1, r+1):
            # 좌상
            # 인덱스 범위 내에 있으면서 퀸이 있는지
            if (r-j) >= 0 and (i-j) >= 0 and board[r-j][i-j] == 1:
                is_place = False
                break

            # 우상
            # 인덱스 범위 내에 있으면서 퀸이 있는지
            if (r - j) >= 0 and (i + j) < N and board[r - j][i + j] == 1:

                is_place = False
                break

        # 세로, 대각선 검사 완료했는데 i번째 열에 퀸을 놓을 수 있으면
        if is_place == True:
            # 현재 위치에 놓고 다음 위치 r+1행으로 이동(재귀호출)
            board[r][i] = 1
            backtracking(r+1, remain-1)  # 퀸 하나 놓았으니 남은 개수 빼주기
            board[r][i] = 0  # 초기화

    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    cnt = 0

    backtracking(0, N)
    print(f'#{tc} {cnt}')