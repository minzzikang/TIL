T = 10
for tc in range(1, T+1):
    # 100 * 100 행렬
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 합의 최대값 (배열 전체를 순회해야 구할 수 있으므로 반복문 밖에 위치, 한 번만 구하면 되서 초기화 한번)
    max_sum = 0

    # 각 행의 합 구하기
    for i in range(100):  # 행 기준 순회
        sum_row = 0  # 행이 바뀌면 행의 합 초기화
        for j in range(100):
            sum_row += arr[i][j]

        # 방금 구한 행의 합이 max_sum 보다 크면 max_sum 값 갱신
        if sum_row > max_sum:
            max_sum = sum_row

    # 각 열의 합 구하기
    for j in range(100):
        sum_col = 0  # 열이 바뀌면 열의 합 초기화
        for i in range(100):
            sum_col += arr[i][j]

        # 방금 구한 열의 합이 max_sum 보다 크면 max_sum 값 갱신
        if sum_col > max_sum:
            max_sum = sum_col

    # 각 대각선의 합 구하기 (2차원 배열 모두 순회 하면서 대각선에 해당 하는 값만 더하기)
    # 하나의 대각선은 i = j
    # 다른 대각선은 N의 값에서 1뺀 값이 i + j
    dia1_sum = 0
    dia2_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                dia1_sum += arr[i][j]
            if i + j  == N - 1:
                dia2_sum += arr[i][j]
    max_sum = max_sum if max_sum > dia1_sum else dia2_sum
    '''
    if dia1_sum > max_sum:
        max_sum = dia1_sum
    if dia2_sum > max_sum:
        max_sum = dia2_sum
    '''

    print(f'{tc} {max_sum}')