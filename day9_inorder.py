def inorder(t):
    global result
    if t:  # 정점 범위 내
        inorder(cleft[t])  # 왼쪽 자식으로 이동
        result += node[t]  # 중위 순회에서 할 일(알파벳 뽑기)
        inorder(cright[t])  # 오른쪽 자식으로 이동


T = 10
for tc in range(1, T+1):
    N = int(input())  # 정점의 총 개수

    cleft = [0] * (N+1)
    cright = [0] * (N+1)

    # 노드 번호 <=> 알파벳 변환 표 배열
    node = [0] * (N+1)

    # 정점 정보로 트리 만들기
    for i in range(N):
        # 쪼갠 다음 글자 개수 세기
        info = input().split()
        # 0: 노드 번호, 1: 알파벳, 2: 왼쪽자식, 3: 오른쪽자식
        p = int(info[0])
        l = len(info)

        # 길이가 3 이상이면 자식 처리
        if l >= 3:
            cleft[p] = int(info[2])
            if l == 4:
                cright[p] = int(info[3])

        # 노드번호 p에는 알파벳 저장되어 있음
        node[p] = info[1]

    # 중위 순회하며 문자열 출력
    result = ''
    inorder(1)

    print(f'#{tc} {result}')

