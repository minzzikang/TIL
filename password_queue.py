T = 10
for tc in range(1, T + 1):
    int(input())
    data = list(map(int, input().split()))
    N = 8  # 암호 길이

    # 원형 큐로 풀기
    Q = [0] * (N+1)
    front = rear = 0

    # 처음 n번 큐에 넣기
    for i in range(N):
        rear = (rear+1) % N
        Q[rear] = data[i]

    number = 1  # 사이클 내에서 감소해줄 숫자

    while True:
        # 뒤로 보내기 위해 앞에서 꺼내서
        # number를 빼준 후 뒤에 다시 넣기(감소횟수마다 감소숫자 증가)
        front = (front+1) % N
        item = Q[front]

        item -= number

        # 앞에서 꺼내서 감소시킨 값이 0이하면 비밀번호 완성
        if item <= 0:
            item = 0
            rear = (rear+1) % N
            Q[rear] = item
            break

        else:  # 0보다 크면 맨 뒤에 넣기
            rear = (rear+1) % N
            Q[rear] = item

            number += 1  # 다음에 뺄 수 1씩 증가

            # 싸이클 계산
            if number > 5:  # 5 넘어가면 다시 1부터 시작
                number = 1

        print(f'#{tc}', end = ' ')

        # 원형 큐에서 dequeue 8번 반복
        for i in range(8):
            front = (front + 1) % N
            print(Q[front], end = ' ')
        print()