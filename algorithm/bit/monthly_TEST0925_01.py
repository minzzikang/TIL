T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = list(input())
    key = int(input(), 16)

    H = [0] * N  # 암호화 전 16진수

    for i in range(N):
        H[i] = int(P[i], 16) ^ key


    print(f'#{tc}', end = ' ')
    for x in H:
        print(f'{x:X}', end='')
    print()