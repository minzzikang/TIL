T = int(input())
for tc in range(1, T+1):
    # N*M 배열 크기
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0  # 가장 길이가 긴 구조물

    # 행 우선 순회하면서 값이 1인 칸 개수 세기
    for r in range(N):
        cnt_r = 0  # 각 행에서 1인 칸의 개수 (행 바뀌면 초기화)
        for c in range(M):
            if data[r][c] == 1:
                cnt_r += 1
            else:  # 0을 만났을 때
                if max_v < cnt_r:  # 지금까지 구한 장애물 길이와 최대값 비교
                    max_v = cnt_r

                cnt_r = 0  # 최대값이 아니면 길이 리셋

        if max_v < cnt_r:  # 그 행에서 구한 1인 칸의 개수와 최대값 비교
            max_v = cnt_r

    # 열 우선 순회하면서 값이 1인 칸 개수 세기
    for c in range(M):
        cnt_c = 0  # 각 열에서 1인 칸의 개수 (열 바뀌면 초기화)
        for r in range(N):
            if data[r][c] == 1:
                cnt_c += 1
            else:
                if max_v < cnt_c:
                    max_v = cnt_c
                cnt_c = 0

        if max_v < cnt_c:
            max_v = cnt_c

    print(f'#{tc} {max_v}')