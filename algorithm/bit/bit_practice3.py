# swea 1일차 응용-이진수2
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    # 컴퓨터에서는 실수 N을 2진수로 저장해놓고 우리한테 보여주는 거는 10진수로 보여줌

    bin_str = ''

    while True:  # N이 0이 될때까지 반복
        N *= 2  # 1 << N 와 같은 의미

        if N >= 1:
            bin_str += '1'
            N -= 1  # 1을 2진수로 빼냄

        elif N > 0:
            bin_str += '0'

        elif N == 0:
            break

        if len(bin_str) > 12:
            bin_str = 'overflow'
            break

    print(f'#{tc} {bin_str}')
