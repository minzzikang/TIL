T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0  # 최솟값의 인덱스
    max_idx = 0  # 최댓값의 인덱스

    for i in range(1, N):
        if arr[min_idx] > arr[i]:  # 작은 수는 먼저 나온 위치로 결정
            min_idx = i

        if arr[max_idx] <= arr[i]:  # 큰 수는 마지막 위치로 정함
            max_idx = i

    ans = abs(max_idx - min_idx)
    print(f'#{tc} {ans}')