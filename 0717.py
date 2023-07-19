print(-(2**4))  # 지수의 우선순위가 높아서 먼저 실행되고 이후 음수 부호
print(-(2**4))
print((-2) ** 4)

import keyword

print(keyword.kwlist)

height = 180


# 세제곱 함수
# 입력받은 수를 세제곱하여 반환하는 함수 cube() 만들어보기
def cube(x):
    return x ** 3

print(cube(2))
print(cube(100))

# 사각형 넓이와 둘레 구하는 함수 rec()
def rec(w, h):
    return w * h, 2 * (w + h)

print(rec(30, 20))