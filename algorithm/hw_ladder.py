T = 10
# 사다리 이동 방향(하->우->좌)
dr = [1, 0, 0]
dc = [0, 1, -1]

for _ in range(1, 11):
    tc = int(input())
    ladder = list(map(int, input().split()))
    answer = 0

    for i in range(100):
        if ladder[0][i] == 1:  # 시작 위치 찾기(0행 값이 1인 경우)
            r, c = 0, i
            while r != 99:  # 행이 범위 내 있는 경우

