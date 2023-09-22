def find_set(x):
    # 경로 압축
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

def union(x, y):
    # x 집합의 대표와 y 집합의 대표 찾기
    x = find_set(x)
    y = find_set(y)

    # 큰 쪽이 부모
    if x > y:
        p[y] = x
        return
    else:
        p[x]= y
        return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    p = [_ for _ in range(N+1)]

    for j in range(M):
        union(paper[j*2], paper[j*2+1])

    for k in range(1, N+1):
        find_set(k)

    # print(p)
    # p는 각 번호의 대표 정보가 들어가있음
    # set을 이용해 중복 정보 없애고 0번 인덱스 -1 해주기
    '''
    [0, 2, 2, 4, 4, 5]
    '''
    print(f'#{tc} {len(set(p))-1}')