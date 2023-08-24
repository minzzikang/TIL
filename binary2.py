T = int(input())
for tc in range(1, T+1):
    N = float(input())

    bin_string = ''

    while True:
        N = N * 2   # 2를 곱하는 것은 쉬프트 연산자와 같은 의미

        if N >= 1:
            bin_string += '1'
            N -= 1

        elif N > 0:
            bin_string += '0'

        elif N == 0:
            break

        if len(bin_string) > 12:
            bin_string = 'overflow'
            break

    print(f'#{tc} {bin_string}')
