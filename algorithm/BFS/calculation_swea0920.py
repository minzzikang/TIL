from collections import deque

def bfs():
    q = deque()
    visited = [0] * 1000001  # 연산 결과는 100만 이하 숫자이므로 모든 계산 결과 담을 수 있음(중복 없게)

    visited[N] = 1  # 시작 방문 처리
    q.append(N)
    cnt = 0  # 연산 횟수

    while q:
        # bfs 단계 나누기
        size = len(q)

        # size 만큼 반복하면 한 사이클 끝
        for _ in range(size):
            now = q.popleft()

            if now == M:  # 연산을 통해 M이 됐을 때
                return cnt

            # 연산한 결과 Q에 넣기
            if 0 < now + 1 <= 1000000 and not visited[now+1]:
                q.append(now+1)
                visited[now+1] = 1
            if 0 < now - 1 <= 1000000 and not visited[now-1]:
                q.append(now-1)
                visited[now-1] = 1
            if 0 < now * 2 <= 1000000 and not visited[now*2]:
                q.append(now*2)
                visited[now*2] = 1
            if 0 < now - 10 <= 1000000 and not visited[now-10]:
                q.append(now-10)
                visited[now-10] = 1

        cnt += 1  # 연산 횟수 증가

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print(f'#{tc} {bfs()}')