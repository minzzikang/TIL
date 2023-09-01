T = int(input())
di = [-1,1,0,0]
dj = [0,0,-1,1]

for tc in range(1, T+1):
    N = int(input())  # 방 배열 크기
    room_num = [list(map(int, input().split())) for _ in range(N)]
    # 주어진 배열을 순회하면서 상하좌우 방면에 기준 칸보다 1 큰 수가 있으면 +1
    # 연속한 1의 개수 +1 => 최대로 움직일 수 있는 방의 개수
    c = [0] * (N*N + 1)  # 방번호는 1부터 시작

    for i in range(N):
        for j in range(N):
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < N and 0 <= nj < N and room_num[ni][nj] == room_num[i][j] + 1:
                    c[room_num[i][j]] = 1

    # print(count)

    max_cnt = 0
    min_start = 0
    cnt = 0  # 연속한 1의 개수를 셀 변수

    # 카운트 배열의 뒷부분부터 확인하면 방 번호 갱신이 쉬움
    for i in range(N*N, 0, -1):
        if c[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
                min_start = i

            elif max_cnt == cnt:
                min_start = i
        else:  # 카운트 값이 없으면
            cnt = 0

    print(f'#{tc} {min_start} {max_cnt+1}')