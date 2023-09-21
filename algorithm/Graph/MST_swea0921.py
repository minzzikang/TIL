from heapq import heappop, heappush

def prim(s):
    heap = []  # 최소 힙
    MST = [0] * (V+1)  # visited 역할

    heappush(heap, (0, s))  #(가중치, 정점)

    sum_v = 0  # 가중치 누적합

    while heap:
        w, v = heappop(heap)

        if MST[v]:  # 이미 신장트리에 정점 v가 포함됐다면
            continue

        # 포함 안된 정점은 방문체크
        MST[v] = 1

        # 방문한 적 없고, 최소 가중치이므로 누적합에 추가
        sum_v += w

        for next in range(V+1):
            # v에서 next에 갈 수 없거나 next가 이미 신장트리에 포함됐으면
            if graph[v][next] == 0 or MST[next]:
                continue

            # 인접해있고, 아직 신장트리에 포함되지 않았으면 heap에 추가
            heappush(heap, (graph[v][next], next))

    return sum_v


T = int(input())
for tc in range(1, T+1):
    # V: 마지막 노드 번호, E: 간선 개수
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        # s: 시작 정점, e: 도착 정점, w: 가중치
        s, e, w = map(int, input().split())
        graph[s][e] = w
        graph[e][s] = w

    print(f'#{tc} {prim(0)}')