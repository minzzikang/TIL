def inorder(t):
    if t:  # 노드 번호 t가 완전 이진 트리 범위 내 있다면
        if node[t] in ['+', '-', '/', '*']:  # 노드 값에 연산자가 있다면
            # 왼쪽자식과 오른쪽 자식의 값으로 연산
            left = inorder(cleft[t])
            right = inorder(cright[t])

            if node[t] == '+':
                return left + right
            elif node[t] == '-':
                return left - right
            elif node[t] == '*':
                return left * right
            elif node[t] == '/':
                return left / right

        else:  # 정수면
            return node[t]  # 노드의 값 그대로 반환


T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점 개수
    cleft = [0] * (N+1)
    cright = [0] * (N+1)
    node = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        # 0: 노드번호, 1: 연산자 또는 숫자, 2: 왼쪽자식, 3: 오른쪽자식
        p = int(info[0])  # 노드 번호 부모에 저장

        if info[1] in ['+', '-', '/', '*']:  # 연산자일 경우
            node[p] = info[1]  # 부모 노드 번호에 연산자 그대로 저장
            cleft[p] = int(info[2])  # 부모노드의 왼쪽 자식에 값 저장
            cright[p] = int(info[3]) # 부모노드의 오른쪽 자식에 값 저장

        else:  # 정수일 경우
            node[p] = int(info[1])  # 부모 노드 번호에 형변환해서 정수 저장


    result = inorder(1)
    print(f'#{tc} {result}')