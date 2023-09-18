import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    visited = [0] * 101  # 1~100번까지 중복연락 안되도록 체크
    Q = []

    # 시작점 연락 체크
    Q.append(s)
    visited[s] = 1

    while Q:  # 큐가 빌 때까지 반복해서 탐색
        t = Q.pop(0)

        # 이미 큐에 들어가 있으면 중복 삽입x
        # 연결되어 있는 정점 중 가장 빠른 쪽으로 선택
        for i in contact[t]:  # t와 연결되어 있는 모든 정점에 대해 탐색
            if not visited[i]:  # 아직 방문 안 했으면
                Q.append(i)
                visited[i] = visited[t] + 1



T = 10
for tc in range(1, T+1):
    # E: 노드 개수, s: 시작점
    E, s = map(int, input().split())
    data = list(map(int, input().split()))
    contact = [[] for _ in range(101)]  # 인접리스트(번호 1~100)

    for i in range(E):
        contact[data[i*2]].append(data[i*2+1])

    print(f'#{tc} {bfs(s)}')