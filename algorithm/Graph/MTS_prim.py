'''
V E
7 11
f t w
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import heapq  # 우선순위 큐 구현을 위한 라이브러리

def prim(start):
    heap = []
    # MST에 포함되었는지 여부 (visited 역할)
    MST = [0] * V

    # (가중치, 정점 정보) 넣기
    # heap에서 튜플은 앞에 원소를 기준으로 정렬하기 때문에 가중치가 맨 앞으로 와야함
    heapq.heappush(heap, (0, start))
    sum_weight = 0  # 누적합

    while heap:
        # 가장 적은 가중치를 가진 정점 꺼냄
        weight, v = heapq.heappop(heap)

        if MST[v]:  # 이미 방문한 곳이면 pass
            continue

        MST[v] = 1  # 방문 체크
        sum_weight += weight

        # 해당 정점에서 갈 수 있는 노드 체크
        for next in range(V):
            # 갈 수 없거나 이미 갔디면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            # 방문 가능한 지점이면 heap에 추가
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight


V, E = map(int, input().split())
# 인접 행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    # 무방향이라서 양쪽에 값 넣기
    graph[f][t] = w
    graph[t][f] = w

# print(graph)
print(prim(0))