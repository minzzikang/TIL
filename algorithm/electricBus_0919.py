T = int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    N = temp[0]  # 정류장 개수
    battery = temp[1:]
    # print(battery)

    cnt = 0  # 최소 교환 횟수(출발지는 포함x)
    current = 0  # 현재 정류장

    # 종점 도착할때까지 반복
    while current < N-1:  # 인덱스이므로 -1 해주기
        # 종료 조건: 현재 정류장에서 바로 종점 갈 수 있는 경우
        # 다음에 갈 정류장 번호 = 현재 정류장 번호 + 현재 정류장에 있는 충전지 용량
        if current + battery[current] >= N-1:
            break  # while문 종료(충전지 교환 횟수 없음)

        # 현재 정류장에서 갈 수 있는 정류장 중 충전지 용량이 최대값인 정류장 찾기
        charge = 0  # 최대 충전지 용량(=해당 정류장에서 최대로 갈 수 있는 정류장 번호)
        # 현재 정류장의 다음 정류장 ~ 충전지 용량으로 갈 수 있는 범위
        for i in range(current+1, current+battery[current]+1):
            if charge <= i + battery[i]:
                charge = i + battery[i]
                current = i  # 현재 정류장 갱신

        cnt += 1  # 배터리 교체


    print(f'#{tc} {cnt}')