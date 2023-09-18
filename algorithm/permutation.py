numbers = [1,2,3,4,5]
n = len(numbers)

# i번째 원소 자리를 바꿔가며 순열 생성
# 자리 바꿀 수 있는 경우의 수

def perm1(i):
    # 종료 조건
    if i == n:
        print(numbers)
        return

    # 재귀 호출
    # j 선택시 중복 방지를 위해 i보다 뒤에 있는 원소만 선택

    # i,j가 같을 수 있음 (=자리 안바꾸는 경우) => range 지정 시 i+1로 시작하면 안됌
    for j in range(i, n):
        # 현재 위치 i에서 다른 위치 j에 있는 숫자와 자리 바꿈
        numbers[i], numbers[j] = numbers[j], numbers[i]

        # i번째 원소를 누구랑 바꿀지 정했다면 i+1번째 원소를 바꾸러 감
        perm1(i+1)

        # i번째와 j번째 원소를 다시 되돌려놓고 다음 진행 (중복 방지를 위해)
        numbers[i], numbers[j] = numbers[j], numbers[i]




# 순열의 i번째 자리 지정하는 방법
# i번째 자리를 누구로 선택 했는지 기억해야 중복 방지
# 순열 : selected = [0] * n

def perm2(i, selected):
    # 종료 조건
    if i == n:
        print(numbers)
        return

    # 재귀 호출
    # 현재 위치 i에 누구를 놓을 것인지 선택
    # 이전에 선택했던 원소는 선택 x
    for j in range(n):
        # j번째 원소 선택한 적 없다면
        if numbers[j] not in selected:  # 숫자 간에 중복 없다는 조건 하에 가능
            # j번째 원소를 순열의 i 위치에 놓기
            selected[i] = numbers[j]

            # i+1번째에 누구 놓을지 정하러 가기
            perm2(i+1, selected)

            # i번째 위치에 놓았던 거 없던일로 하고 다른 j 선택하러 감
            selected[i] = 0