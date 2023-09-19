def BFS(s, V):   # s: 시작정점, V: 마지막 정점 번호 (= 정점의 개수)
    visited = [0] * (V+1)  # 중복 방문 방지를 위한 방문 체크 배열
    Q = []
    Q.append(s)  # 시작정점 인큐
    visited[s] = 1  # 시작정점 방문 처리

    while Q:  # 큐에 정점이 남아있으면 계속 탐색
        # 큐에서 방문할 곳 하나 꺼내기 (맨 앞에서)
        t = Q.pop(0)
        # 방문한 정점 t에서 할일
        print(t)

        # 현재 정점 t에서 연결된 모든 정점 w를 탐색
        for w in adj_l[t]:
            # 아직 인큐되지 않은 정점 w가 있다면(방문한 적 없으면)
            if not visited[w]:
                # 인큐하고 인큐됐다고 표시(=방문처리)
                Q.append(w)
                # 지나온 간선 개수를 알 수 있음
                # 정점 t에서 지나온 간선 개수에서 +1
                visited[w] = visited[t] + 1

        '''
        for w in range(1, V+1):
            if adj_m[t][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[t] + 1
        '''

V, E = map(int, input().split())  # V: 마지막 정점 번호, E: 간선 개수
graph = list(map(int, input().split()))

# 인접리스트로
adj_l = [[] for _ in range(V+1)]  # 0번 인덱스 사용 x
for i in range(E):
    start, to = graph[i*2], graph[i*2+1]  # start: 시작, to: 목적지
    # 무방향이라 서로 연결
    adj_l[start].append(to)
    adj_l[to].append(start)


# 인접 행렬로
adj_m = [[0] * (V+1) for _ in range(V+1)]
for i in range(E):
    start, to = graph[i*2], graph[i*2+1]
    # 무방향이라 서로 연결
    adj_m[start][to] = 1
    adj_m[to][start] = 1

BFS(1, V)