N = int(input())  # 보드 크기
K = int(input())  # 사과 개수
apple_li = [tuple(map(int, input().split())) for _ in range(K)]  # 사과 좌표 (순서 상관없음)
L = int(input())  # 뱀 방향 변환 횟수
dlst = [input().split() for _ in range(L)]  # 뱀 방향 정보 (초, 방향)
dtable = [0] * 10000  # 방향 전환에 사용될 참조 테이블

for sec, turn in dlst:
    dtable[int(sec)] = turn

di, dj = [-1,0,1,0], [0,1,0,-1]  # 시계방향
dr = 1  # 초기 방향(오른쪽)

snake = [(1,1)]
ans = 0

while True:
    ans += 1
    ci, cj = snake[0]  # 뱀의 현재 머리 좌표
    ni, nj = ci+di[dr], cj+dj[dr]  # 뱀이 갈 다음 방향 좌표

    # 벽에 부딪히지 않고, 자기 자신과도 안 만나면
    if 1 <= ni <= N and 1 <= nj <= N and (ni, nj) not in snake:
        snake.insert(0, (ni, nj))  # 머리는 항상 가장 앞에(0번 자리에)

        if (ni, nj) in apple_li:  # 사과를 만날 경우
            apple_li.remove((ni, nj))
        else:  # 사과를 못 만나면
            snake.remove((snake[-1]))  # 꼬리 부분 제거

        # 방향 전환
        if dtable[ans] == 'D':  # 오른쪽으로 회전
            dr = (dr+1) % 4
        elif dtable[ans] == 'L':  # 왼쪽으로 회전
            dr = (dr+3) % 4
    else:
        break

print(ans)