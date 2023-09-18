def solve(idx, N, s, K):
    global cnt
    # 종료 조건
    if idx == N:  # 주어진 수열의 각 자리를 모두 정함(넣을지 말지)
        if s == K:  # 정해진 자리(부분수열)의 각 수의 합이 K이면 카운트
            cnt += 1

    elif s > K:  # 지금까지 구한 합들이 K보다 크면 정답이 될 수 없음
        return

    else:
        solve(idx+1, N, s+A[idx], K)  # 이전 단계까지 구한 합 s에 idx+1의 값을 포함시킴
        solve(idx+1, N, s, K)  # idx+1을 포함시키지 않음


T = int(input())
for tc in range(1,T+1):
    # 합이 K가 되는 부분수열 갯수 구하기
    # 수열의 길이는 N
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    solve(0,N,0,K)
    print(f'#{tc} {cnt}')
