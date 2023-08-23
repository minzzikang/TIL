bit = '0000000111100000011000000111100110000110000111100111100111111001100111'
n = len(bit)

# 7칸씩 쪼개서 십진수 만들기
for i in range(0, n, 7):
    bit7 = bit[i:i+7]  # i번째부터 7번째까지
    # print(bit7)

    base = 2  # 지수의 밑
    ex = 0  # 거듭제곱
    dec = 0  # 십진수로 바꾼 결과 (여기에 누적합)

    for j in range(6,-1,-1):  # 비트의 뒤에서부터 계산
        if bit7[j] == "1":  # 문자열로 입력 받았으므로
            dec += base ** ex
            ex += 1
        else:
            ex += 1

    print(dec, end = ' ')