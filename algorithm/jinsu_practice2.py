hex1 = '0F97A3'
hex2 = '01D06079861D79F99F'

def solution(hex_string):
    # 2진수 문자열로 바꾸면 길이 * 4
    l = len(hex_string) * 4

    # 16진수 문자열을 숫자로 바꾸기
    x = int(hex_string, 16)

    print(x)    # 1021859 / 33461878848289896863

    # 7칸씩 잘라서 이진수로 만든 뒤 이진수 출력
    # 이진수를 10진수로 바꾸고 출력
    for i in range(l-1, -1, -7):  # 뒷 자리부터 출력해야하므로(첫번째 오는게 2의 l-1 승)
        bin_string = ''

        # l-1-0, l-1-1, l-1-2, l-1-3, ... , l-1-6
        for j in range(7):
            if i-j < 0:  # 자를 비트가 7개 미만 남았을 경우
                break
            # i-j번째 비트 판별(j가 증가하면서 i값 감소)
            if x & (1 << i - j) == 0:
                bin_string += '0'
            else:
                bin_string += '1'

        # 2진수 문자열을 10진수로 바꾸기
        dec = int(bin_string, 2)
        print(dec, end = ': ')

        print(bin_string, end = ', ')
    print()





solution(hex1)
'''
0000111 1100101 1110100 011
7 101 116 3
'''
solution(hex2)
'''
0000000 1110100 0001100 0000111 1001100 0011000 0111010 1111001 1111100 1100111 11 
'''