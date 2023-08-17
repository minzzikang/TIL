T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 정수 개수, M: 구간 개수
    arr = list(map(int, input().split()))

    max_v = 0  # 최대 구간합
    min_v = 1000 * M  # 최소 구간합 (구간이 가질 수 있는 최대값으로 설정-최악의 경우)

    # 주어진 숫자 배열을 순회하면서 구간합 구하기
    for i in range(N-M+1):  # 구간의 첫 시작이 갈 수 있는 인덱스 범위 (0 -> N-M)
        # 현재 구간의 합 (다음 구간으로 가면 초기화)
        now_sum = 0
        
        for j in range(M):  # M: 0 -> M-1
            now_sum += arr[i+j]
        
        # 반복문 끝나서 현재 구간합이 최종으로 구해지고 난 후 조건문 실행
        if max_v < now_sum:  # 현재 구간합이 최대 구간합보다 크면 값 갱신
            max_v = now_sum
        
        if min_v > now_sum:  # 현재 구간합이 최소 구간합보다 작으면 값 갱신
            min_v = now_sum

    print(f'#{tc} {max_v - min_v}')