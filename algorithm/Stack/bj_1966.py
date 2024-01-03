# 프린터 큐
from collections import deque
import sys

T = int(input())
for tc in range(T):
    # N : 문서 개수, M : 정답을 구해야하는 문서의 현재 큐에서의 위치
    N, M = map(int, input().split())
    important = deque(list(map(int, sys.stdin.readline().split())))

    cnt = 0

    while important:
        max_value = max(important)
        front = important.popleft()
        M -= 1

        if max_value == front:
            cnt += 1

            if M < 0:  # 가장 왼쪽이 0번째이므로 0보다 작으면 출력되었음
                print(cnt)
                break

        else:
            important.append(front)  # 순서 뒤로 밀려남
            if M < 0:  # 밀려날 때 자리가 맨 앞이면 제일 뒤로 이동
                M = len(important) - 1

