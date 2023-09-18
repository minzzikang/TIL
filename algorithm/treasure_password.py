T = int(input())
for tc in range(1, T+1):
    # N: 보물 상자 뚜껑에 적힌 숫자 개수
    # K: 만든 비밀번호 중 K번째로 큰 수가 정답
    N, K = map(int, input().split())
    number = list(input())

    # 4변으로 나눠서 시계방향으로 회전해서 만든 비밀번호를 담을 리스트
    turn = []

    l = N // 4  # 회전해야 하는 수는 숫자 개수에서 4변으로 나눈 만큼(이후는 숫자 생성이 반복됨)

    for _ in range(l):
        # 0번 위치(맨앞)에 맨 뒤 pop한 숫자 추가
        temp = number.pop()
        number.insert(0, temp)

        # 한 변에 들어가는 숫자 = 생성될 비밀번호
        for i in range(0, N, l):
            password = ''

            for j in range(i, i+l):
                password += number[j]
            turn.append(password)  # 비번 만들어지면 리스트에 넣기

    set_turn = set(turn)  # 중복 요소 제거
    # print(set_turn)
    '''
    {'5E1', '1F7', '1B3', 'E1B', 'B81', '81F', 'F75', '3B3', 'B3B', '3B8', '75E'}
    '''

    new_num = []  # 16진수 문자열의 비번을 10진수로 바꿔서 담을 리스트 (set은 정렬이 안되서)

    # 16진수 문자열을 10진수 숫자로 바꾸기
    for t in set_turn:
        new_num.append(int(t, 16))

    new_num.sort(reverse=True)  # 내림차순으로 정렬(k번째 큰 수 구하기 위해)
    # print(new_num)

    # K는 0부터 시작해서 1을 빼줌
    print(f'#{tc} {new_num[K-1]}')