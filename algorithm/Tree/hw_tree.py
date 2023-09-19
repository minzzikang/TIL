def inorder(t):
    if t:
        inorder(tree[t*2])  # 왼쪽 먼저 방문
        print(tree[t][1], end = '')  # t 들러서 할일 하기
        inorder(tree[t*2+1])  # 오른쪽 방문


T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 총 개수
    tree = [list(input().split()) for _ in range(N)]

    print(f'#{tc}', end = ' ')
    inorder(1)
    print()
