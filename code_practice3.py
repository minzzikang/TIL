pat = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9,
}

hex1 = '0DEC'
hex2 = '0269FAC9A0'

def find_code(hex_stirng):
    l = len(hex_stirng) * 4  # 16진수는 4비트로 표현, 16진수가 4글자면 *4만큼 비트 필요
    x = int(hex_stirng, 16)  # 컴퓨터한테 16진수라고 알려줌. 그럼 문자열도 숫자로 인식해서 2진수로 저장.

    bin_string = ''

    # i번째 비트 검사해서 결과가 0이면 i번째 비트는 0 / 아니면 1
    for i in range(l-1, -1, -1):
        # hex1에서 x가 3564인데 이것을 2진수로 표현할 때
        if x & (1 << i):
            bin_string += '1'
        else:
            bin_string += '0'

    # print(x)  # 우리 눈에는 10진수로 보이지만 컴퓨터에는 2진수로 저장되어 있음
    print(bin(x))
    print(bin_string)

    bin_list = list(bin_string)  # 가변 타입으로 변경

    result = ''
    # 뒤에서부터 검사해서 1 만나면 암호 해독
    for j in range(l-1, 5, -1):  # j: 0 -> 5
        # 1을 만나는 순간 6개씩 잘라서 검사
        if bin_list[j] == '0':
            continue

        # 1을 만났다
        code = ''.join(bin_string[j-5:j+1])

        # 6개 잘라온 코드가 암호사전에 있는지 확인
        dec = pat.get(code)  # 코드가 안에 없으면 None 출력

        if dec != None:
            result += str(dec) + ' '

            # 암호코드로 변경한 나머지 5칸에서 패턴을 또 찾지 않도록 처리
            for i in range(j, j-6, -1):  # j: 0 -> 5
                bin_list[i] = '0'

    print(result[::-1])

find_code(hex1)
find_code(hex2)