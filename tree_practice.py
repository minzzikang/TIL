def preorder(node):
    global cnt

    if node:  # 노드가 있으면(왼쪽자식/오른쪽자식)
        cnt += 1  # 노드 개수 +1
        preorder(c_left[node])
        preorder(c_right[node])

T = int(input())
for tc in range(1, T+1):
    # E: 간선 개수, N: 루트 노드 번호
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))
    cnt = 0  # 서브트리에 속한 노드 개수

    # 부모 노드를 인덱스 번호로 노드끼리 연결하기
    c_left = [0] * (E+2)  # c_left[i] => i의 왼쪽 자식 노드번호
    c_right = [0] * (E+2)

    for i in range(E):
        p, c = tree[i*2], tree[i*2+1]

        if c_left[p] == 0:  # 왼쪽자식 먼저 채우기
            c_left[p] = c
        else:
            c_right[p] = c

    preorder(N)

    print(f'#{tc} {cnt}')