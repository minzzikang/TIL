def counting_sort_asc(A, B, K):
    # A: 정렬 대상
    # B: 정렬 결과
    # K: 정렬 대상 중 최댓값
    C =[0] * (K+1)  # 카운트 배열(원소 개수 세고 자리 정해줌)
    # C[x] = x의 등장 횟수

    # 1. 각 원소 등장 횟수
    for i in range(len(A)):
        # A[i]의 등장 횟수 하나씩 증가
        C[A[i]] += 1  # A[i]가 들어갈 자리 가리킴

    # 2. 각 원소 등장 횟수 계산 후 각 원소가 들어갈 자리 위치 구함
    for i in range(1, len(C)):
        # i는 i보다 작은 수 몇 개 있는 지 알아보는 과정
        C[i] += C[i-1]  # 누적합

    # 3. 뒤에서부터 A 확인하며 자리 확인하고 채움(안전 정렬)
    # 자리 채울 때마다 1씩 감소(자리 중복 피하기 위해)
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        [C[A[i]]] = A[i]

nums = [0, 4, 1, 3, 1, 2, 4]
result_arr = [0] * 8
counting_sort_asc(nums, result_arr, max(nums))
print()

