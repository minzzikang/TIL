def dfs(start):
    # 종료 조건
    if len(lst) == M:
        print(' '.join(map(str, lst)))
        return

    # 재귀 호출
    for i in range(start, N+1):
        if i not in lst:
            lst.append(i)
            dfs(i+1)
            lst.pop()

N, M = map(int, input().split())

lst = []  # 조건 만족하는 수열

dfs(1)
