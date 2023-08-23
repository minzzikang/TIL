T = int(input())
for tc in range(1, T+1):
    # N: 퍼즐 크기, K = 단어 길이
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 행 우선 순회로 가로에 들어갈 자리 찾기
    for r in range(N):
        cnt_r = 0  # 각 행에서 1인 칸 개수 세기 (행 바뀌면 초기화)
        for c in range(N):
            if puzzle[r][c] == 1:
                cnt_r += 1
            else:  # 0을 만난 경우
                if cnt_r == K:  # 여태까지 센 1의 칸 개수와 단어 길이 같은지 확인
                    ans += 1
                cnt_r = 0  # 길이 다르면 0으로 초기화(다시 세기 시작)

        if cnt_r == K:  # 퍼즐 크기만큼 다 살펴본 후 그 행에서의 최종 1인 칸과 단어 길이 비교
            ans += 1


    # 열 우선 순회로 세로에 들어갈 자리 찾기
    for c in range(N):
        cnt_c = 0
        for r in range(N):
            if puzzle[r][c] == 1:
                cnt_c += 1

            else:  # 칸 수 더하다 0을 만나면 길이 같은 지 확인하기
                if cnt_c == K:
                    ans += 1
                cnt_c = 0  # 길이 같지 않는 경우 리셋

        if cnt_c == K:
            ans += 1

    print(f'#{tc} {ans}')