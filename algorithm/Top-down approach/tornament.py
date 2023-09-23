scissors = 1
rock = 2
paper = 3

def tournament(i, j):
    # 종료조건 : 더 이상 두 부분으로 쪼갤 수 없을 때
    # i~j 사이에 있는 사람 1명
    if i == j:
        return i

    # 재귀호출
    else:
        # 왼쪽 부분
        left = tournament(i, (i+j)//2)
        # 오른쪽 부분
        right = tournament((i+j)//2 + 1, j)

        # 왼쪽과 오른쪽 중 승자 골라서 return
        # cards[left] => 왼쪽 사람이 낸 패
        # cards[right] => 오른쪽 사람이 낸 패

        # 승자 판별 코드
        winner = 0
        if cards[left] == 1:
            if cards[right] == 3 or cards[right] == 1:
                winner = left
            else:
                winner = right
        elif cards[left] == 2:
            if cards[right] == 1 or cards[right] == 2:
                winner = left
            else:
                winner = right
        else:
            if cards[right] == 2 or cards[right] == 3:
                winner = left
            else:
                winner = right

        return winner  # winner는 인덱스 값이므로 나중에 결과값에 1 더해줘야 함(1번 학생부터 시작)


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 인원 수
    cards = list(map(int, input().split()))

    result = tournament(0, N-1)

    print(f'#{tc} {result + 1}')