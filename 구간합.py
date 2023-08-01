T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))  # 구간합을 구해야 하는 정수 배열

    sum_li = []  # 구간합의 누적을 담을 리스트

    for i in range(N-M+1):  # 길이가 N인 배열에서 M씩 묶어서 반복하는 범위
        result = 0

        # j부터 M까지의 범위에서 결과값에
        for j in range(j, j+M):
            result += arr[j]
        sum_li.append(result)

    sub = max(sum_li) - min(sum_li)
    print(f'#{tc} {sub}')