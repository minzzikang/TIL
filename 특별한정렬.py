T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 최대/최소값 위치(인덱스)
    idx = 0

    # 선택 정렬
    for i in range(10):  # 10개까지만 정렬
        # i 위치에 올 원소
        numbers[i] = numbers[idx]

        # i 뒤에 있는 원소부터 최대/최소 찾기 시작
        for j in range(1, N):  # 10개 이후에 위치할 수 있으므로

            # i가 짝수일 때 => 최대값
            if i % 2 == 0:
                

            # i가 홀수일 때 => 최솟값
        
        # 최대/최솟값 인덱스
        idx = 

        # i번째 원소는? idx번째랑 자리 교환

    # numbers를 앞에서부터 10개만 출력