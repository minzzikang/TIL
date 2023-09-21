def game(r, c, n, arr):
    # 탐색할 방향 (하->우->좌->상)
    dr = [1,0,0,-1]
    dc = [0,1,-1,0]

    stack = []  # 가장 최근 방문점을 저장
    visited = [[0] * n for _ in range(n)]  # 방문 체크 배열

    visited[r][c] = 1  # 시작점 방문 체크

    while True:
        if arr[r][c] == 3:
            return 1  # 길 찾기 성공

        for d in range(4):
            # 다음 방향 탐색
            nr = r + dr[d]
            nc = c + dc[d]

            # 다음에 갈 방향이 배열 범위 안에 있고, 벽(1)이 아니고, 방문한 적이 없으면
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and visited[nr][nc] == 0:
                stack.append((r, c))  # 잘못됐을 때 돌아올 위치 저장(현재 위치)
                visited[nr][nc] = 1  # 방문 체크
                r, c = nr, nc  # 현재 위치 갱신
                break  # 새로운 위치에서 탐색하기 위해 반복문 빠져나감

        else:  # 4방향 탐색 완료(길 없음)
            if stack:
                r, c = stack.pop()  # 최근 위치로 되돌아가기
            else:
                return 0  # 탐색 완료 (탈출 실패) - while문 종료



T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 미로 크기
    data = [list(map(int, input())) for _ in range(N)]  # 미로 정보

    # 시작 위치 찾기
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                r, c = i, j  # 시작점 찾으면 그 위치를 변수에 저장

    print(f'#{tc} {game(r, c, N, data)}')