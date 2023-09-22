# 격자판의 숫자 이어 붙이기
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 특정 위치를 기점으로 상하좌우(델타 활용) 문자(num)를 붙여야 해서
# 파라미터로 좌표값 전달해줘야 함
def dfs(r, c, num):
    # 종료 조건
    if len(num) == 7:  # 7개 다 고르면
        ans.add(num)
        return

    # 재귀 호출
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if not(0 <= nr < 4 and 0 <= nc < 4):
            continue

        dfs(nr, nc, num + arr[nr][nc])


T = int(input())
for tc in range(1, T+1):
    arr = [input().split() for _ in range(4)]
    # print(arr)
    ans = set()  # 중복 제거를 위해

    # 시작 지점이 정해져있지 않음
    # 반복문으로 모두 확인
    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(ans)}')