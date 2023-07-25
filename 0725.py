# 비시퀀스 데이터구조
# dict method

# mutable data 복사
# 1. 할당 : 객체의 주소(참조)를 복사
# 2. 얕은 복사 : slicing[:]  슬라이싱 객체는 원복 객체와 독립적으로 존재
#               내장함수.copy()
# 얕은 복사의 한계: 중첩 리스트
import copy

a = [1, 2, [1, 2]]
b = a[:]
b[2][0] = 99
print(a, b)

# 깊은 복사
deep_copied_list = copy.deepcopy(a)


# immutable data 복사