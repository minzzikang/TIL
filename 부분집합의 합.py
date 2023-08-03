T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]

for tc in range(1, T+1):
    # N: 부분집합 중 원소의 개수
    # K: 부분집합 원소의 합
    N, K = map(int, input().split())

    count = 0  # 원소 합과 개수가 일치하는(조건만족) 부분집합 개수

    # 집합 A의 모든 부분집합을 검사
    for i in range(1 << len(A)): # i는 
        sum_set = 0  # 부분집합의 합
        count_set = 0  # 부분집합의 개수
        # 부분집합 중 i번째에는 n개의 원소 중 j번째의 원소를 포함하는지 
        for j in range(N):  # 원소의 개수 N개만큼 비트값 비교
            if i & (1 << j):  # 1을 j번만큼 옮겼을 때 부분집합인 i와 일치하는지 확인
                count_set += 1
                sum_set += A[j]
        
            if sum_set == K and count_set == N:
                count += 1
            
    print(f'#{tc} {count}')
