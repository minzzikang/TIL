#케빈 베이컨의 6단계 법칙
N, M = map(int, input().split())  # N: 유저 수, M: 친구 관계 수
relationship = [[] for _ in range(N+1)]

for _ in range(1, M+1):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)

# print(relationship)