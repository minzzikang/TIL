import sys
sys.stdin = open('input.txt', 'r')

def bfs(s):
    visited = [0] * 101  # 1~100번까지 중복연락 안되도록 체크
    Q = [s]

    # 시작점 연락 체크
    visited[s] = 1

    max_v = 0  # 마지막 연락(visited에서 가장 큰 숫자)
    last_num = 0  # 마지막에 연락 받은 사람의 번호

    while Q:  # 큐가 빌 때까지 반복해서 탐색
        now = Q.pop(0)

        # 이미 큐에 들어가 있으면 중복 삽입x
        # 연결되어 있는 정점 중 가장 빠른 쪽으로 선택
        for next in contact[now]:  # 현재 정점 now와 연결되어 있는 모든 정점에 대해 탐색
            if visited[next]:
                continue

            Q.append(next)
            # 기존 방문보다 한 번 더 갔다고 표시
            visited[next] = visited[now] + 1

            # 전화를 더 했거나 전화 받은 순서는 같은 데 번호가 더 크면
            # max값 초기화
            if max_v < visited[next] or (max_v == visited[next] and last_num < next):
                max_v = visited[next]
                last_num = next

    return last_num


T = 10
for tc in range(1, T+1):
    # E: 노드 개수, s: 시작점
    E, s = map(int, input().split())
    data = list(map(int, input().split()))
    contact = [[] for _ in range(101)]  # 인접리스트(번호 1~100)

    for i in range(E//2):
        contact[data[i*2]].append(data[i*2+1])

    # print(contact)
    print(f'#{tc} {bfs(s)}')