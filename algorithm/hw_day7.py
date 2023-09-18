T = 10
for tc in range(1, T+1):
    int(input())
    data = list(map(int, input()))

    Q = [0] * 100000
    front = rear = -1
    password = ''

    # 입력받은 값 그대로 Q에 추가
    for i in range(8):
        rear += 1
        Q[rear] = data[i]

    while True:
        for j in range(1, 6):  # 싸이클 1~5회마다 각 회차만큼 숫자 감소
            front += 1
            temp = Q[front]
            rear += 1
            Q[rear] = temp - j

            # 감소해서 뒤로 이동한 값이 0보다 작거나 같아지면
            if Q[rear] <= 0:
                Q[rear] = 0  # 0으로 하고 멈춤
                break

        if Q[rear] == 0:  # 마지막에 추가한 값이 0일 경우
            for a in range(front+1, rear+1):  # 뒤로 이동시키기 위해 지정한 front 값의 오른쪽 값부터 rear 값까지
                password += str(Q[a])  # 문자열로 형변환
            break


    print(f'#{tc}', *password)

