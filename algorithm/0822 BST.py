'''
7
9 4 9 12 4 3 4 6 12 15 15 13 15 17
'''

cleft = [0] * 20
cright = [0] * 20

E = int(input())  # 간선 개수
tree = list(map(int, input().split()))

for i in range(E):
    p, c = tree[i * 2], tree[i * 2 + 1]

    # 루트 기준
    # 루트보다 작으면 왼쪽 자식 / 크면 오른쪽 자식
    if p < c:
        cright[p] = c
    else:
        cleft[p] = c


def search(node, key):  # 재귀함수
    if key == node:
        print(f'find : {node} == {key}')
        return node
    elif key > node:
        print('right', node, cright[node])
        return search(cright[node], key)
    else:
        print('left', node, cleft[node])
        return search(cleft[node], key)


def search2(node, key):  # 반복문
    # 노드가 있는 경우
    while node:
        if key == node:
            print(f'find : {node} == {key}')
            return node

        elif key > node:
            print('right', node, cright[node])
            return search(cright[node], key)

        else:
            print('left', node, cleft[node])
            return search(cleft[node], key)

    # 여기까지 코드가 실행됐다는 것은 리턴을 못 만난 것(key 가 tree에 없음)
    return None  # 탐색 실패


print(search(9, 13))
print(search2(9, 13))



# =========================================================

# 최대 힙
arr = [10,6,4,5,1,3,2,9,7,8]

heap = [0] * 11  # 0번 인덱스 사용 x

# 마지막에 넣을 원소 위치 비교할 변수 필요
last = 0

# 삽입 연산
def enq(item):
    global last
    last += 1  # 마지막 위치에 원소 추가

    heap[last] = item

    # 원소 추가한 이후 조건 만족하는지 확인 (부모 > 자식)
    # 현재 위치를 자식 노드로 생각, 부모노드 위치 계산(자식 // 2)
    c = last
    p = c // 2

    # 자리 바꾸려면 부모 노드 존재하고, 자식이 부모보다 작을때까지 위치 교환
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]

        # 자식과 부모 위치를 그 위로 바꾸고 그 위의 부모랑도 비교
        c = p
        p = c // 2

# 삭제 연산
def deq():
    global last
    # 원소가 하나 사라지므로 자리를 당겨줘야함
    # 루트 노드 삭제할 건데
    temp = heap[1]

    # 마지막 노드를 루트 위치에 당겨옴
    heap[1] = heap[last]

    # 원소 삭제했으니 라스트 당김
    last -= 1

    # 루트부터 자리 찾아가기 시작
    p = 1
    c = p * 2  # 왼쪽 자식 기준(완전 이진 트리는 왼쪽부터 채워가기 때문)

    # 자리조정
    # 최대 힙은 부모가 자식보다 큼(작을 경우 계속 자리 교환)

    # 왼쪽 자식의 인덱스가 last보다 작아야 tree 내에 존재하는 것
    while c <= last:
        # 오른쪽 자식이 있고 그게 왼쪽보다 클때
        if c + 1 <= last and heap[c] < heap[c+1]:
            c = c + 1  # 비교 대상을 왼쪽 => 오른쪽으로 변경

        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = c * 2

        else:  # 부모가 자식보다 커지면
            break  # 자기 자리 찾은 것

    return temp  # 자리 다 정해졌으니 루트 노드 반환




for i in range(10):
    enq(arr[i])

print(heap)