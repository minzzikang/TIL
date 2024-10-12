N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B에서 최대값과 A에서 최소값이 곱해져야 최소합을 구할 수 있음
A.sort()
temp = B[:] # B를 훼손하지 않기 위한 복사본 배열
sum_v = 0

for i in range(N):
    # temp에서의 최대값을 가진 인덱스 찾기
    max_idx = temp.index(max(temp))
    sum_v += A[i] * temp[max_idx]
    temp[max_idx] = -1  # 사용 후 -1로 바꾸기

print(sum_v)