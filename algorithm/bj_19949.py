answers = list(map(int, input().split()))
select = []  # 영재가 선택한 답 모음
cnt = 0  # 5점 이상인 경우의 수

def backtracking(n):
    if len(select) == 10:  # 답 선택 끝
        total = 0  # 문제 맞힌 점수
        for i in range(10):
            if answers[i] == select[i]:
                total += 1
        if total >= 5:  # 5점 이상일때만 경우의 수 추가
            global cnt
            cnt += 1
    else:
        for i in range(1,6):  # 5지 선다
            if check(i):
                select.append(i)
                backtracking(n+1) # n+1번째 답 선택
                select.pop()

def check(m):
    # 세 번 연속 같은 답 선택X
    if len(select) >= 2 and select[-1] == m and select[-2] == m:
        return False
    return True

backtracking(1)  # 첫 번째 답 선택
print(cnt)