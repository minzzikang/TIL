def dfs(r, c):
    dr = [-1,-1,0,1,1,1,0,-1]
    dc = [0,1,1,1,0,-1,-1,-1]

    stack


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    stack = []
    cnt = 0

    for _ in range(h):
        stack.append(list(map(int, input().split())))

    for r in range(w):
        for c in range(h):
            if arr[r][c] == 1:
                dfs(r, c)
                cnt += 1

