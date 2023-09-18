def check(player):
    for p in player:
        if p == 3:
            return True

    for i in range(len(player) - 2):  # 번호 8,9는 run이 될 수 없음
        # 연달아 값이 있다 = run
        if player[i] and player[i+1] and player[i+2]:
            return True


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    # 플레이어한테 카드 일단 나눠주지 말것. (먼저 만드면 6장 안받아도 게임 가능하므로)
    # 각 플레이어 별로 카드 번호 몇 장씩 있는지 확인 하기 위한 리스트
    p1 = [0] * 10
    p2 = [0] * 10

    print(f'#{tc}', end = ' ')

    for i in range(12):
        if i % 2 == 0:
            p1[card[i]] += 1
            if check(p1):  # run 또는 triplet 나오면 승리
                print('1')
                break
        else:
            p2[card[i]] += 1
            if check(p2):  # run 또는 triplet 나오면 승리
                print('2')
                break

    else:  # 정상 탐색 했는데 승자 안 나오면 무승부
        print('0')