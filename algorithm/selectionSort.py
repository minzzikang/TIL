# selection_sort(i) : i번째 자리에 놓을 리스트에서 i번째로 작은 원소 찾기
# 리스트 길이가 5라면?
# selection_sort(0): 0번 인덱스에 제일 작은 원소 놓기
# selection_sort(1): 1번 인덱스에 그 다음으로 작은 원소 놓기
# .....
# selection_sort(4): 4번 인덱스에 그 다음으로 작은 원소 놓기
# selection_sort(5): 5번 인덱스는 리스트 범위 벗어남

def selection_sort(i, lst):
    # 종료 조건
    if i == len(lst):  # 인덱스 범위 벗어날 때 함수 종료
        return

    # i번 인덱스에서 해야 할 일
    min_i = i  # 제일 작은값 인덱스를 i로 지정
    # 제일 작은 값 찾아서 i번 인덱스에 놓기
    for j in range(i+1, len(lst)):
        if lst[min_i] > lst[j]:
            min_i = j

    # 자리 바꾸기
    lst[i], lst[min_i] = lst[min_i], lst[i]

    # 재귀 호출 (i+1번 인덱스에 놓을 작은 원소 찾으러)
    selection_sort(i+1, lst)


lst = [3,2,4,5,1]
selection_sort(0, lst)

print(lst)