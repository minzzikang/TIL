import sys
sys.stdin = open('sample_input.txt', 'r')

# 암호 비율 딕셔너리
code_dict = {
    (2,1,1) : 0,
    (2,2,1) : 1,
    (1,2,2) : 2,
    (4,1,1) : 3,
    (1,3,2) : 4,
    (2,3,1) : 5,
    (1,1,4) : 6,
    (3,1,2) : 7,
    (2,1,3) : 8,
    (1,1,2) : 9
}

T = int(input())
for tc in range(1, T+1):
    # N*M 배열 크기
    N, M = map(int, input().split())
    res = 0  # 출력할 결과
    # 암호 코드 + 중복 제거(arr의 요소 중에 겹치는 것이 많음)
    arr = set([input()[:M] for _ in range(N)])  # M의 범위 벗어나는 입력값 때문

    # 중복 제거한 arr의 요소 하나씩 검사
    for i in range(len(arr)):
        # i번째 줄에서 검사
        ith_row = arr[i]

        # i번째 줄 16진수 문자열을 2진수 문자열로 바꾸기
        bin_row = ''

        # i번째 줄 문자열에서 문자 하나씩 떼서 2진수 문자열로
        for c in ith_row:
            c_hex_to_dec = int(c, 16)  # 16진수라고 알려주기

            for j in range(3, -1, -1):  # 인덱스 3부터 0번까지
                # 2진수의 큰 수인 왼쪽부터 출력해야해서 최대로 민 다음 거슬러(오른쪽으로) 올라가며 비교
                bin_row += '1' if c_hex_to_dec & (1<<j) else '0'

        # i번째 문자열을 2진수로 바꿨는데 안에 1이 없다면
        if '1' not in bin_row:
            continue  # 다음 줄 검사

        else:
            # i번째 줄 안에 1이 있으면 뒤에서부터 암호코드 만들기 시작
            # 0과 1의 비율 (0 1 0 1 번갈아가며 나옴)
            ratio = [0] * 4
            '''
            ratio[0] : 맨 처음 0의 비율
            ratio[1] : 두 번째 1의 비율
            ratio[2] : 세 번째 0의 비율
            ratio[3] : 마지막 1의 비율
            '''

            # 끝에서 1이 시작되기 전의 0은 필요없어서 제거
            bin_row.rstrip('0')

            # 모든 코드는 끝이 1이므로 뒤에서부터 비율 계산
            for k in range(len(bin_row)-1, -1, -1):
                # 맨 마지막의 1을 세고 있는거면 그 이전의 0을 센 적이 없어야 함.
                if bin_row[k] == '1' and ratio[2] == 0:
                    # 마지막 1의 비율 계산 중..
                    ratio[3] += 1
                # 세 번째 0을 세고 있는 거면 그 이전(두번째)의 1을 센 적이 없어야 함.
                elif bin_row[k] == '0' and ratio[1] == 0:
                    # 세 번째 0의 비율 계산 중..
                    ratio[2] += 1
                # 두 번째 1을 세고 있는 거면 그 이전(첫번째)의 0을 센 적이 없어야 함.
                elif bin_row[k] == '1' and ratio[0] == 0:
                    # 두 번째 1의 비율 계산 중..
                    ratio[1] += 1
                # 처음 부분의 0을 만났을 때(이전 부분이 1이여야 함)
                elif bin_row[k] == '0' and bin_row[k-1] == '1':
                    # 첫 0은 비율 계산 필요 x(나머지 3부분의 비율로 코드 확인 가능)
                    min_v = min(ratio[1:4])  # 제일 작은 수 구해서 나누기
                    # 비율 계산 후 그 비율로 된 숫자가 딕셔너리에 있는지 확인
                     number = code_dict.get((ratio[1] // min_v, ratio[2] // min_v, ratio[3] // min_v))