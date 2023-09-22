# find_set, union 사용
def find_set(x):  # x의 대표 찾기
    if x != p[x]:
        p[x] = find_set(p[x])

    return p[x]

def union(x, y):
    # 각 집합의 대표 찾기
    x = find_set(x)
    y = find_set(y)

    # 대표가 더 크면 부모
    if x > y:
        p[y] = x
        return

    else:
        p[x] = y
        return


T = int(input())
for tc in range(1, T+1):
    # N: 마을 사람 수, M: 서로 아는 관계 수
    N, M = map(int, input().split())

    p = [_ for _ in range(N+1)]  # make_set


    for _ in range(M):
        num1, num2 = map(int, input().split())
        union(num1, num2)

    # print(p)
    '''
    [0, 5, 5, 4, 6, 5, 6]
    '''
    for i in range(1, N+1):
        find_set(i)

    # print(p)
    '''
    [0, 5, 5, 6, 6, 5, 6]
    '''

    print(f'#{tc} {len(set(p))-1}')