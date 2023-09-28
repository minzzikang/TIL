numbers = [1,2,3,4,5,6,7,8,9,10]

selected = [0] * 10
# select[i] == 1  => i번째 원소를 부분집합에 포함o
# select[i] == 0  => i번째 원소를 부분집합에 포함x

n = len(numbers)

x = 10
# 만약 합이 x보다 작은 부분집합만 구해야 한다면?
# i번째 원소를 선택o/선택x 했던 상황에서 합을 기억


# 재귀함수로 부분집합 구하기
# i번째 원소를 부분집합에 포함시킬지 말지 결정
# n-1번째 원소까지하고, 다 완료한 경우 뒤로 돌아와서
# 내가 이전에 선택했다면 선택 안하고 다음 진행 ... 반복

def subset(i, subsum):
    # 0. 최적화(다른 조건)
    if subsum > x:
        return   # 더 이상 진행x (가지치기)

    # 1. 종료 조건: n개의 원소에 대한 선택을 끝냄 (부분합에 넣던지 안넣던지)
    if i == n:
        temp = 0  # 합을 기억하기 위한 변수
        for j in range(n):
            if selected[j]:  # j번째 원소를 부분집합에 포함시켰으면
                temp += numbers[j]  # j번재 원소를 부분집합의 합에 더함

        # 합이 x 이하인 부분집합만 출력
        if temp <= x:
            for j in range(n):
                if selected[j]:
                    print(numbers[j], end = ' ')
            print()

        return

    # 2. 재귀호출
    # i번째 원소 선택하고 다음 i+1번째 원소 선택하러 가거나
    selected[i] = 1
    subset(i+1, subsum + numbers[i])  # 선택했으니 i번째 원소값을 더해줘야함

    # i번째 원소 선택하지 않고 다음 i+1번째 원소를 선택하러 가거나
    selected[i] = 0
    subset(i+1, subsum)


subset(0, 0)