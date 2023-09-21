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
from heapq import heappop, heappush  # 우선순위 큐 구현을 위한 라이브러리

def prim(start):
    heap = []  # 최소힙(루트가 최솟값, 원소 꺼내면 루트가 꺼내짐)

    # 신장트리에 포함시킨 정점 정보 (visited 역할)
    MST = [0] * V

    # (가중치, 정점) 정보 넣기
    # 튜플은 앞에 원소를 기준으로 정렬하기 때문에 가중치가 맨 앞으로 와야함
    heappush(heap, (0, start))

    # 가중치 누적합(최소 신장 트리)
    min_w = 0

    while heap:
        # 가장 적은 가중치를 가진 정점 꺼냄
        # 힙을 사용했기 때문에 반복문 돌면서 최소 가중치 정점 찾을 필요 x
        w, v = heappop(heap)

        if MST[v]:  # 정점 v가 이미 신장트리에 포함되어있으면 pass
            continue

        # 신장트리에 포함 안 된 정점 v 꺼낸 경우
        MST[v] = 1  # 방문 체크

        # 방금 꺼낸 정점과 가중치는 연결된 적 없고, 최소 가중치를 가졌으므로 누적합에 추가
        min_w += w

        # 해당 정점(v)와 연결된 모든 노드 확인
        for next in range(V):
            # v에서 next로 갈 수 없거나 이미 신장트리에 포함됐다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue

            # 인접해있고, 신장트리에 포함된 적 없으면 heap에 추가 (후보군)
            heappush(heap, (graph[v][next], next))

    return min_w


V, E = map(int, input().split())
# 인접 행렬 (정점 0번 포함)
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    # f: 시작, t: 도착, w: 가중치
    f, t, w = map(int, input().split())
    # 무방향이라서 양쪽에 값 넣기
    graph[f][t] = w
    graph[t][f] = w

# print(graph)
print(prim(0))