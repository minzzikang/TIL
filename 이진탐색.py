def binarySearh(arr, P, key):
    start = 1
    end = P  # 주어진 전체 페이지
    count = 0

    while start <= end:
        count += 1  # 페이지 탐색과 동시에 탐색 횟수 1 추가
        center = (start + end) // 2
        if arr[center] == key:  # 찾기 성공
            return count
        elif arr[center] > key:
            end = center
        else:
            start = center

    return False


T = int(input())
for tc in range(1, T+1):
    # P: 전체 페이지
    # Pa: A가 찾을 쪽번호
    # Pb: B가 찾을 쪽번호
    P, Pa, Pb = map(int, input().split())

    # A 탐색 시작
    binarySearh(P, Pa, )

    # B 탐색 시작
    binarySearh()
