def enq(item):  # 삽입 연산
    global last
    last += 1

    heap[last] = item  # 일단 item 추가

    # 현재 위치를 자식 노드라고 생각하면, 부모 노드 위치 계산
    c = last
    p = c // 2

    # 부모가 자식보다 작을 때까지 위치 교환(부모 노드 존재)
    while p and heap[c] < heap[p]:
        heap[c], heap[p] = heap[p], heap[c]

        # 자식과 부모 위치를 그 위로 바꾸고 그 위의 부모와도 비교
        c = p
        p = c // 2

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 노드 개수
    node = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0  # 마지막에 넣을 원소 위치 비교할 변수
    ans = 0

    for i in node:
        enq(i)

    while last > 0:  # 노드 길이가 얼마나 될지 모르니까 last가 루트까지 갈때까지 반복
        last //= 2  # 부모 노드를 찾아가기 위함
        ans += heap[last]

    print(f'#{tc} {ans}')