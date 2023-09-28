T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0] + [list(map(int, input().split())) for _ in range(N+1)]

    visited = [0] +