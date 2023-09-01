T = int(input())
for tc in range(1,T+1):
    B = input()
    ternary = list(map(int, input()))
    ans = 0

    len_bin = len(B)
    len_ter = len(ternary)

    binary = int(B, 2)  # 2진수라고 알려줌

    # XOR연산(^): 각 자릿수 비교해서 다르면 1, 같으면 0
    # 각 비트를 반전시킨 2진수 만들기
    bin_li = [0] * len_bin
    for i in range(len_bin):
        bin_li[i] = binary ^ (1<<i)

    # print(bin_li)
    '''
    [11, 8, 14, 2]
    '''

    # 3진수 ternary[i] 자리를 바꾼 숫자 만들기
    for i in range(len_ter):
        num1 = 0  # (ternary[i]+1) % 3
        num2 = 0  # (ternary[i]+2) % 3

        for j in range(len_ter):
            if i != j:  # 바꾸지 않아도 될 경우
                num1 = num1 * 3 + ternary[j]
                num2 = num2 * 3 + ternary[j]
            else:  # 바꿔야 하는 자리수일 경우
                num1 = num1 * 3 + (ternary[j] + 1) % 3
                num2 = num2 * 3 + (ternary[j] + 2) % 3

        if num1 in bin_li:
            ans = num1
            break  # 자리 바꾸는 작업 멈춤

        if num2 in bin_li:
            ans = num2
            break

    print(f'#{tc} {ans}')
