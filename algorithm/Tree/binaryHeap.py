def inorder(t, N):
    global num
    if t <= N:  # t번 노드가 노드 개수를 벗어나면 안됌
        inorder(t * 2, N)
        tree[t] = num  # 중위 순회에서 할 일 (num을 tree의 t번 노드에 할당)
        num += 1  # 다음 중위 순회의 노드를 위해 num을 + 1 해줌
        inorder(t * 2 + 1, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드 개수(완전 이진 트리)
    tree = [0] * (N+1)

    # 1~N까지 1씩 증가하며 완전 이진트리를 중위순회로 만들기
    num = 1

    inorder(1, N)

    print(f'#{tc} {tree[1]} {tree[N//2]}')