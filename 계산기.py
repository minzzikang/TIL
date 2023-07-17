# 계산기 프로그램
# 사용할 수 있는 연산자
# +, -, *, /
# %(나머지), //(몫)

# 1. 두 숫자를 먼저 입력받는다.
# 2. 연산자를 입력받는다.
# 3. 결과를 출력
# 주의해야 할 점 : 나눗셈은 0으로 나누기 불가능(ZeroDivisionError)
# 한번 계산이 끝나고 또 계산 이어갈 수 있도록 반복문 사용
# 계산기 끝내는 조건 : 두 숫자 모두 0 입력했을 때

print(
    """
 _   _      _ _       _ _
| | | | ___| | | ___ | | |
| |_| |/ _ \ | |/ _ \| | |
|  _  |  __/ | | (_) |_|_|
|_| |_|\___|_|_|\___/(_|_)
"""
)

while True:
    a, b = map(int, input("숫자를 입력하세요 : ").split())
    print(a, b)

    if (a == b and a == 0):
        print("종료")
        break

    cal = input("연산자를 입력하세요 : ")

    plus = a + b
    minus = a - b
    multiply = a * b

    if cal == "+":
        print(f"결과 : {plus}")
    elif cal == "-":
        print(f"결과 : {minus}")
    elif cal == "/":
        if b == 0:
            print("0으로는 나눌 수 없습니다.")
        else:
            print("결과 : ", a / b)
    elif cal == "*":
        print(f"결과 : {multiply}")
    elif cal == "%":
        print("결과 : ", a % b)
    elif cal == "//":
        print("결과 : ", a // b)
    else:
        print("연산자를 잘못 입력했습니다.")


