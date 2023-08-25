T = int(input())
for tc in range(1, T+1):
    S = input()  # 영준이가 가진 카드 정보

    # 각 4가지 무늬의 1~13 까지 카드 몇 장 가지고 있는지 확인하는 카운팅 배열
    count = [[0] * 14 for _ in range(4)]
    # 스페이스-다이아-하트-클로버
    shape = {'S': 0, 'D': 1, 'H': 2, 'C': 4}

    # 입력받은 카드 정보 쪼개기
    for i in range(0, len(S), 3):
        # 카드 타입을 알려주는 알파벳을 변수에 담기 (나중에 인덱스로 쓰기 위해)
        type = shape[S[i]]
        num = int(S[i+1 : i+3])  # 카드 정보의 i+1, i+2는 카드 번호

        if count[type][num]

