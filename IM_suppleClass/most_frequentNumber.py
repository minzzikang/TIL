T = int(input())
for tc in range(1, T+1):
    int(input())
    grade = list(map(int, input().split()))
    count = [0] * 101  # 0~100점 빈도 저장할 카운팅 배열

    # 학생 1000명의 점수에서 각 점수가 몇 번 나오는지
    for i in range(1000):
        count[grade[i]] += 1  # 카운팅 배열의 인덱스는 각 학생의 점수

    # 카운팅 배열에서 가장 많은 값을 가지는 인덱스 찾기
    max_idx = 0  # 우선 0번째 인덱스라고 가정

    for j in range(1, 100):
        if count[max_idx] <= count[j]:  # 여러 개 일 땐 큰 점수 출력
            max_idx = j

    print(f'#{tc} {max_idx}')