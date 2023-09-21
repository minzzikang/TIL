# 출발과 도착 정점 사이 최단 거리 구하는 함수
def bfs(S, V):
    # 정점 방문 중복 방지를 위한 방문 체크 배열
    visited = [0] * (V+1)
    Q = []

    # 시작 정점 큐에 넣고 방문 체크
    Q.append(S)
    visited[S] = 1

    while Q:  # 큐가 빌 때까지 반복
        # 방문할 정점 꺼내기
        t = Q.pop(0)

        if t == G:  # 방문할 정점이 도착점이랑 같으면
            return visited[t] - 1  # 지나온 노드 개수 반환

        for i in adj_l[t]:  # 현재 방문 중인 정점 t에서 인접한 정점들 탐색
            # 아직 방문 안했으면 큐에 추가하고 방문하기
            if not visited[i]:
                Q.append(i)
                visited[i] = visited[t] + 1  # 현재 정점 t에서 i로 가면서 노드 지나온 개수 + 1

    return 0  # 연결 안 됐으면 0 출력


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())  # V: 노드 개수, E: 간선 개수
    adj_l = [[] for _ in range(V+1)] # 0번 인덱스 사용x

    # 입력받은 data로 인접리스트 만들기
    for _ in range(E):
        s, e = map(int, input().split())
        adj_l[s].append(e)
        adj_l[e].append(s)

    S, G = map(int, input().split())  # S: 출발 노드, G: 도착 노드

    print(f'#{tc} {bfs(S, V)}')