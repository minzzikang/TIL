# prim이랑 다른 점은 누적 거리를 구한다는 점
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
from heapq import heappush, heappop

N, M = map(int, input().split())
# 인접리스트
graph = [[] for _ in range(N)]

for _ in range(M):
    f, t, w = map(int, input().split())
    graph[f].append([t,w])

# 누적 거리를 계속 저장할 리스트
INF = int(1e9)
distance = [INF] * N  # distance[t]는 처음에 무한대로 초기화해놔서 계산한 적 있는지도 확인 가능

def dijkstar(start):
    pq = []  # 우선순위 큐
    heappush(pq, (0, start))  # 출발점 초기화 (가중치, 정점)
    distance[start] = 0

    while pq:
        # 현재 시점에서 누적 거리(가중치)가 가장 짧은 노드 정보 꺼내기
        dist, now = heappop(pq)

        # 현재 노드까지의 거리(가중치)가 이전에 계산한 누적 최소거리보다 크면 pass
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적 있다면 pass
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # 다음 노드로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크다면 pass
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heappush(pq, (new_cost, next_node))

dijkstar(0)
print(distance)
