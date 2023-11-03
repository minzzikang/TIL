T = int(input())
for tc in range(1, T+1):
    # m*n 행열
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    cnt = 0  # 이동 횟수

    for r in range(n):
       floor = m-1  # 바닥(총 이동횟수에서 뺌)
       for c in range(m-1, -1, -1):  # 바닥부터 역순으로 확인
           if arr[r][c] == 1:
               cnt += floor - c
               floor -= 1

    print(cnt)
