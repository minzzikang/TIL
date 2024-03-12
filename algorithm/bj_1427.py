N = list(map(int, input()))

ans = sorted(N, reverse=True)

for _ in ans:
    print(_, end='')
