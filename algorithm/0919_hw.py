def merge(l, r):
    global cnt
    result = []

    # 왼쪽 리스트 마지막 원소가 오른쪽 리스트 마지막 원소보다 클 때
    if l[-1] > r[-1]:
        cnt += 1

    # i: l에서 원소 꺼낼 위치 / j: r에서 원소 꺼낼 위치
    i, j = 0, 0

    while True:
        # i와 j가 0번째 인덱스부터 하나씩 이동하면서 작은 값 먼저 결과리스트에 추가함
        # 왼쪽/오른쪽 리스트 길이를 인덱스가 벗어나면 반복 끝
        if len(l) > i and len(r) > j:  # 둘 다 값이 있는 경우
            # 왼쪽 리스트의 i번째가 오른쪽 리스트의 j번째 값보다 작거나 같으면
            if l[i] <= r[j]:
                # 결과 리스트에 왼쪽 리스트 요소를 추가
                result.append(l[i])
                i += 1  # 왼쪽 리스트의 다음 요소 확인

            else:  # 왼쪽 리스트의 i번째 오른쪽 리스트의 j번째보다 클때
                result.append(r[j])
                j += 1  # 오른쪽 리스트의 다음 요소 확인

        # 둘 중 하나의 리스트에 값이 남은 경우
        elif len(l) > i:
            for m in range(i, len(l)):  # m: i -> len(l)-1
                result.append(l[m])
                i += 1

        elif len(r) > j:
            for n in range(j, len(r)):  # n: j -> len(r)-1
                result.append(r[n])
                j += 1

        else:  # 병합 완료(while문 종료)
            break

    return result

def merge_sort(lst):
    # 종료 조건: 더 이상 분할 안 될 때까지
    if len(lst) == 1:
        return lst

    # 리스트 분할 및 정렬
    mid = len(lst) // 2
    l = lst[:mid]
    r = lst[mid:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0  # 오른쪽 원소가 먼저 복사 되는 경우의 수

    ans = merge_sort(L)

    print(f'#{tc} {ans[N//2]} {cnt}')