# is 비교 연산자
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)  # 겉보기 값은 같지만 참조하는 주소가 다름


# 매개변수와 인자의 차이
def add_numbers(x, y):  # x, y는 매개변수(parameter)
    result = x + y
    return result

a= 2
b = 3
sum_result = add_numbers(a, b)  # a, b는 인자(argument)
print(sum_result)


# 위치 인자 (함수 호출 시 반드시 값 전달)
def greet(name, age):
    print(f'안녕하세요 {name}님! {age}살이시군요.')

greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.


# 기본 인자 (햠수 호출 시 인자 전달 안하면 기본값이 매개변수에 할당)
def greet(name, age=30):  # age에 인자 전달 안하면 기본값인 30이 출력
    print(f'안녕하세요 {name}님! {age}살이시군요.')

greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.


# 키워드 인자
greet(age=25, name='Alice')  # 인자 순서 상관 x
#greet(age=25, 'Dave')  # SyntaxError ; positional argument follows keyword argument
# 키워드 인자는 위치 인자 이후 사용해야 함


# 임의의 인자 목록
def calculate_sum(*args):
    print(args)

calculate_sum(1, 2, 3, 4, 5)


num = 100
def my_func():
    print(num)

my_func()  # local scope에 변수 선언 안해서 바깥 영역에서 찾아옴

# 재귀 함수
def factirial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과 반환 
    return n * factirial(n - 1)

result = factirial(5)
print(result)  # 120