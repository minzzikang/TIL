T = int(input())
for tc in range(1, T+1):
    N, hexa = input().split()
    N = int(N)

    binary = ''  # 이진수로 바꾼 결과 (합하기)

    for i in range(N):
        hex_to_dec = int(hexa[i], 16)  # 입력받은 hexa의 요소 하나를 16진수로 보고 그에 해당하는 10진수로 바꿔줌

        for j in range(3, -1, -1):  # 비트는 뒤에서부터 채워지는데 출력은 앞에서부터 해야하므로
            if hex_to_dec & (1 << j):  # j번째 비트가 1인지
                binary += "1"
            else:
                binary += "0"

    print(f'#{tc} {binary}')