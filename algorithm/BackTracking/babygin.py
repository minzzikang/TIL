def is_triple(lst):
    return lst[0] == lst[1] and lst[1] == lst[2]

def is_run(lst):
    return lst[0] == lst[1]-1 and lst[1] == lst[2]-1

def babyGin(idx, used, lst):
    # 종료 조건
    if idx == 6:  # 인덱스 범위 벗어나면 다 고른 것
        front = [lst[i] for i in used[:3]]
        back = [lst[i] for i in used[3:]]

        if (is_run(front) or is_triple(front)) and (is_triple(back) or is_run(back)):
            print(f'Baby Gin {front} {back}')

        return

    # 재귀 호출
    for i in range(6):
        if i not in used:  # i번째 숫자가 아직 사용되기 전이면
            used.append(i)  # i번째 숫자 사용처리
            babyGin(idx+1, used, lst)
            used.pop()  # 다른 자리에서 쓰기 위한 초기화

T = 4
for _ in range(1, T+1):
    card = list(map(int, input()))
    used = [0] * 6  # 숫자 사용 여부 확인

    babyGin(0, [], card)