# 모든 간선 중 가중치 가장 적은 것 우선으로 고르기
# 단, 사이클이 발생하지 않도록 (union find)
V, E = map(int, input().split())
# 인접 리스트 활용
edge = []

for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f,t,w])

# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])

p = [_ for _ in range(V)]

def find_set(x):
    if p[x] == x:
        return x

    p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:  # 사이클 발생!
        return

    if x < y:
        p[y] = x

    else:
        p[x] = y

cnt = 0  # 현재 방문한 정점 수
sum_weight = 0
for f, t, w in edge:
    # 사이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)

        if cnt == V:  # MST 구성 끝
            break


print(sum_weight)