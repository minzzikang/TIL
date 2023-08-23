# 후위 순회 (왼쪽 오른쪽 자식의 값을 모두 확인해야 하므로)
def postorder(t):
    if t:  # 노드 번호 t가 완전 이진 트리 범위 내 있다면
        if node[t] in ['+', '-', '/', '*']:  # t번 노드 값에 연산자가 있다면
            # 왼쪽자식과 오른쪽 자식의 값으로 연산
            left = postorder(cleft[t])
            right = postorder(cright[t])

            if node[t] == '+':
                node[t] = left + right
            elif node[t] == '-':
                node[t] = left - right
            elif node[t] == '*':
                node[t] = left * right
            elif node[t] == '/':
                node[t] = left / right

            return node[t]  # 반환한 결과값은 상위 레벨에서 다시 쓰일수도..

        else:  # 정수면
            return node[t]  # 노드의 값 그대로 반환 (반환해서 상위 레벨에서 쓰임)


T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점 개수
    cleft = [0] * (N+1)
    cright = [0] * (N+1)
    node = [0] * (N+1)

    for _ in range(N):
        info = input().split()
        # 0: 노드번호, 1: 연산자 또는 숫자, 2: 왼쪽자식, 3: 오른쪽자식
        t = int(info[0])  # 노드 번호

        if info[1] in ['+', '-', '/', '*']:  # 연산자일 경우 자식 존재
            node[t] = info[1]  # 연산자 그대로 저장
            cleft[t] = int(info[2])  # 왼쪽 자식에 정수값 저장
            cright[t] = int(info[3]) # 오른쪽 자식에 정수값 저장

        else:  # 숫자일 경우
            node[t] = int(info[1])  # 부모 노드 번호에 형변환해서 정수 저장


    result = postorder(1)
    print(f'#{tc} {int(result)}')