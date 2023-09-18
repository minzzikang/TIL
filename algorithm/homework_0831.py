def swap(cnt):
    global ans

    val = int(''.join(number))

    if (cnt, val) in visited:  # change번 자리 바꾸기 진행하면서 만든 적 있는 숫자면 진행x
        return


    # 만든 적 없는 숫자면 만들었다고 체크 하고 진행
    visited.add((cnt, val))

    if cnt == change:
        ans = max(ans, val)
        return

    # 자리를 바꿀 위치 2개를 교환 할 때마다 새로 지정해줘야 함
    # 동일한 위치에서 중복 교환 허용하기 때문
    for i in range(len(number) - 1):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]
            swap(cnt + 1)
            # 자리 원상 복구(새로운 i,j 찾기 위해)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T + 1):
    number, change = input().split()
    number = list(number)
    change = int(change)

    # 중복 체크
    visited = set()  # (k, num): 자리를 k번 교환했을 때 num을 만든 적이 있다.
    ans = 0

    swap(0)

    print(f'#{tc} {ans}')