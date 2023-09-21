from heapq import heappush, heappop

def dijkstar(s):
    pq = []
    heappush(pq, (0, s))  # (가중치, 정점)
    distance[s] = 0  # 출발점에서 출발점까지 거리는 0

    while pq:
        dist, now = heappop(pq)

        # 방금 꺼낸 가중치(거리) 정보가 이전에 누적으로 구한 최소거리보다 크면 pass
        if distance[now] < dist:
            continue

        # 현재 정점(now)에 인접한 정점들 확인
        for next, cost in graph[now]:
            new_cost = distance[now] + cost

            if distance[next] <= new_cost:
                continue

            distance[next] = new_cost
            heappush(pq, (new_cost, next))



T = int(input())
for tc in range(1, T+1):
    # N: 마지막 노드 번호, E: 도로(간선) 개수
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    distance = [99999999] * (N + 1)  # 누적 거리 저장 리스트 (무한대로 초기화)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append([e, w])

    dijkstar(0)
    print(f'#{tc} {distance[N]}')