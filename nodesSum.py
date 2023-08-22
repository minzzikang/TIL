def postorder(t):
    # 노드 번호 t가 완전 이진 트리 범위 안에 있다면
    # t번 노드에 값이 있음
    # 자식 노드로 더 내려갈 필요 없음
    # t번 노드에 있는 값 return (부모 노드 값 구할 때 필요)
    if t <= N:
        if tree[t]:
            return tree[t]

        else:
            left = postorder(2 * t)
            right = postorder(2 * t + 1)
            tree[t] = left + right
            # 계산 끝나면 결과 반환(그 위의 부모 노드 구할 때 또 써야 함)
            return tree[t]

    return 0


T = int(input())
for tc in range(1, T+1):
    # N: 노드 개수, M: 리프 노드 개수, L: 값 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)

    for _ in range(M):
        node, leaf = map(int, input().split())
        tree[node] = leaf

    postorder(1)
    print(f'#{tc} {tree[L]}')
