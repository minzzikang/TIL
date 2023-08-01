# 탐욕 알고리즘으로 풀이
# counts에 값이 1 이상인 데이터가 3개 이상 있으면 run
# counts 값이 3 이상이면 triplet
num = 456789  # Baby Gin 확인할 6자리 수
# 6자리 수로부터 각 자리 수 추출하여 개수 누적할 리스트
c = [0] * 12  # 0부터 9까지지만 마지막칸에서 T,R 검사하기 위해 여분으로 10,11칸 생성

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:  # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    # run 조사 후 데이터 삭제
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    # triplete도 run도 아닌 경우 옆 칸으로 이동
    i += 1

if run + tri == 2: print('Baby Gin')
else: print('Lose')