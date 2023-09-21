# 모든 간선 중 가중치 가장 적은 것 우선으로 고르기
# 단, 사이클이 발생하지 않도록 (union find) 사용
V, E = map(int, input().split())
# 인접 리스트 활용(정렬하려고)
edge = []

for _ in range(E):
    f, t, w = map(int, input().split())
    edge.append([f,t,w])  # 넣을 때 바로 w를 맨 앞으로 넣어주면 편함

# w를 기준으로 정렬
edge.sort(key=lambda x: x[2])

p = [_ for _ in range(V)]  # make_set 필요 없음

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
sum_w = 0  # 가중치 합

# 정렬된 리스트를 순회하며 가중치가 작은 간선 정보부터 확인
for f, t, w in edge:
    # 사이클이 발생하지 않는다면
    # => f정점과 t정점이 각각 속한 집합의 대표가 달라야 함
    if find_set(f) != find_set(t):
        cnt += 1
        sum_w += w
        union(f, t)

        # MST 구성 끝
        if cnt == V:
            break

print(sum_w)