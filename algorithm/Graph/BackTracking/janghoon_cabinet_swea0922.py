# cnt: 고른 점원의 수 , sum_h: 점원 키의 누적합
def backtracking(cnt, sum_h):
    global ans

    # 최적화(가지치기)
    # 현재까지 탑의 높이(키의 누적합)가 선반 높이 넘어가면 더 쌓을 필요 없음
    if sum_h >= B:
        ans = min(ans, sum_h)
        return

    # 종료 조건
    if cnt == N:
        return

    # 조합 중복 제거해야 함(ex. 1,2 = 2,1)
    # 해당 점원을 탑에 쓸 경우
    backtracking(cnt+1, sum_h + S[cnt])
    # 해당 점원을 탑에 안 쓸 경우
    backtracking(cnt + 1, sum_h)



T = int(input())
for tc in range(1, T+1):
    # N: 점원 수, B: 선반 높이
    N, B = map(int, input().split())
    S = list(map(int, input().split()))  # 점원들의 키
    ans = int(1e9)  # 탑과 선반의 차이가 최소인 값(정답)
    backtracking(0, 0)

    print(f'#{tc} {ans - B}')