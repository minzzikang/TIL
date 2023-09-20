# p[x] : x의 부모
# p[x] == x : x가 속한 집합의 대표가 x
# p[x] != x : x는 x가 속한 집합의 대표가 아님

p = [0] * 7  # 0번 인덱스 사용 x

# 1. 집합 초기화
def make_set(x):
    # 처음 만들 때 집합에 속한 사람이 1명 (자기 자신이 대표)
    p[x] = x

# 2. x가 속한 집합의 대표를 얻는 연산
def find_set(x):
    # 자기 자신의 부모가 자기 자신을 가리킨다면 자기 자신이 대표
    if x == p[x]:
        return x

    # 아닌 경우, 부모의 대표 찾는 것 반복(재귀)
    else:
        return find_set(p[x])

# 3. 두 집합을 합치는 연산
# x가 속한 집합과 y가 속한 집합을 합치는 연산
# x가 속한 집합의 대표와 y가 속한 집합의 대표 둘 중 하나로 대표 통일
def union(x, y):
    p[find_set(y)] = find_set(x)


#==========================================================
p1 = [0] * 7
rank = [0] * 7  # 트리 깊이 저장할 리스트

# 1. 집합 초기화
def make_set1(x):
    p[x] = x
    # 처음 트리 깊이는 0
    rank[x] = 0

# 2. 대표 찾는 연산
def find_set1(x):
    # 경로 압축!!
    if x != p[x]:
        p[x] = find_set1(p[x])

    return p[x]

# 재귀 사용하지 않는 버전
def find_set2(x):
    while x != p[x]:
        x = p[x]

    return x

# 3. 두 집합 합치는 연산
def union1(x, y):
    # x 집합의 대표와 y 집합의 대표 찾기
    x = find_set1(x)
    y = find_set1(y)

    # x 집합과 y 집합 합칠 때 트리 깊이가 더 큰 쪽이 대표
    if rank[x] > rank[y]:
        p[y] = x

    else:
        # 아니면 일단 대표 y로
        p[x] = y
        # 두 집합 깊이가 같은 경우 깊이 + 1
        if rank[x] == rank[y]:
            rank[y] += 1  # y가 부모이므로 y에서만 증가



for i in range(1, 7):
    make_set1(i)

union1(1,3)
union1(2,3)
union1(5,6)
union1(1,5)
print(p)
'''
[0, 3, 3, 6, 4, 6, 6]
'''
print(find_set1(1))
print(p)  # 경로 최적화 이루어짐
'''
[0, 6, 3, 6, 4, 6, 6]
'''