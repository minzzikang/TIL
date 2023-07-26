# 비시퀀스 데이터구조
# dict method

# mutable data 복사
# 1. 할당 : 객체의 주소(참조)를 복사
# 2. 얕은 복사 : slicing[:]  슬라이싱 객체는 원복 객체와 독립적으로 존재
#               내장함수.copy()
# 얕은 복사의 한계: 중첩 리스트
# import copy

# a = [1, 2, [1, 2]]
# b = a[:]
# b[2][0] = 99
# print(a, b)

# # 깊은 복사
# deep_copied_list = copy.deepcopy(a)

# immutable data 복사


#0726 Classes
'''
함수가 직접 호출하는 것이 아닌 객체에 의해 호출되는 형태로 변경

-클래스와 객체의 관계
name = 'Alice'
인스턴스가 메서드 호출 (인스턴스.메서드())
'''
# 클래스 구조
# 클래스 정의
class Person: # 파스칼 케이스 사용(대문자로 시작)
    # 클래스 변수, 모든 인스턴스가 공유
    blood_color = 'red'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    # 생성자 메서드(인스턴스 생성 시 자동 호출, 초기화)
    def __init__(self, name):  # __매직메서드__(개발자가 직접 호출x)
        self.name = name  
    
    def singing(self):
        return f'{self.name}가 노래합니다.'
      
# 인스턴스 생성 (인자 반드시 필요 = name 위치인자)
singer1 = Person('IU')
singer2 = Person('BTS')

# p2 = Person()  # 생성자 메서드 없어도 빈괄호로 변수 할당 가능
# p2.name = 'jisu'

# singer1의 인스턴스 변수 blood_color가 만들어짐
singer1.blood_color = 'green'
print(singer1.blood_color)

# 메서드 호출
print(singer1.singing())  # return 값 가지고 있어서 print 필요
print(singer2.singing())

# 속성(변수) 사용
print(singer1.blood_color)  # 클래스 변수에는 인스턴스로 접근보단 가급적 클래스 이름 통해 접근
print(Person.blood_color)

# 인스턴스 변수는 class가 관여하는 부분이 아님(직접적 접근 불가, 객체 간의 독립성)
# 메서드 생성은 안됨.

# 클래스.클래스변수 형식으로 변경


# 인스턴스 메서드(인스턴스.메서드)
# - 반드시 첫 번째 매개변수로 인스턴스 자신self를 전달받음
# - 인스턴스 변수에 접근 및 수정 가능

# 클래스 메서드(클래스.메서드)
# @데코레이터 사용하며 정의, 호출하는 클래스(cls)가 매개변수로 들어감
# 데코레이터 없으면 인스턴스 메서드로
# 클래스 이름이랑 맞추지 않는 이유는 상속 때문.

# 정적 메서드(=static method)
# @데코레이터 사용하여 정의, 호출시 매개변수 필수 아님.
# 객체, 클래스 상태 수정x 단지 기능만 위한 메서드

# 매직메서드(double underbar)
class MyClass:
    # pass
    def __str__(self):
        return '나는 MyClass다.'
    
c1 = MyClass()
print(c1)

