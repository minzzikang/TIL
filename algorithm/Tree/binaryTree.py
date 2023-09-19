'''
V : 마지막 정점 번호
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

#  전위순회
def preorder(n):
    if n:  # 자식이 존재하는 정점이면
        print(n, end = ' ')  # 방문
        preorder(ch1[n])  # 왼쪽 서브트리로 이동
        preorder(ch2[n])  # 오른쪽 서브트리로 이동


V = int(input())
E = V - 1  # 간선 수는 정점 개수 - 1
tree = list(map(int, input().split()))

# 부모를 인덱스로 자식 저장하기
ch1 = [0] * (V+1)
ch2 = [0] * (V+1)

# 자식을 인덱스로 부모 저장하기
par = [0] * (V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

    if ch1[p] == 0:  # 자식 1이 아직 없으면
        ch1[p] = c
    else:
        ch2[p] = c  # 자식 1이 이미 있으면 자식2에 저장

    par[c] = p  # 자식을 인덱스로 부모 저장


preorder(1)