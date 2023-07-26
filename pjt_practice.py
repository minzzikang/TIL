# # ws_7_2.py

# # 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self, width, height):
#       self.width = width  # 인스턴스 변수 정의/할당
#       self.height = height

#    # 인스턴스 메서드 추가
#    def calculate_area(self):
#       return self.width * self.height
     
# shape1 = Shape(5, 3)  # Shape 클래스의 인스턴스 생성
# area1 = shape1.calculate_area()  # 인스턴스 메서드 호출
# print(area1)


# ws_7_3.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self, width, height):
#       self.width = width
#       self.height = height

#    def calculate_perimeter(self):
#       return (self.width + self.height) * 2

# shape1 = Shape(5, 3)
# perimeter1 = shape1.calculate_perimeter()
# print(perimeter1)

# ws_7_4.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self, width, height):
#       self.width = width
#       self.height = height
      
#    def print_info(self):
#       print(f'Width: {self.width}')
#       print(f'Height: {self.height}')
#       print(f'Area: {self.width * self.height}')
#       print(f'Perimeter: {(self.width + self.height) * 2}')           
      
# shape1 = Shape(5, 3)
# shape1.print_info()


# # 매직메서드
# class Shape:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height

#   def __gt__(self, other):  # 자신 말고 다른 객체 
#     return self.width * self.height > other.width * other.height
  
#   def __eq__(self, other):
#     return self.width * self.height == other.width * other.height

# s1 = Shape(3,4)
# s2 = Shape(5,6)
# print(s2 > s1)

# s3 = Shape(6,5)
# print(s2 == s3)

# ws_7_5.py

# 아래 클래스를 수정하시오.
# class Shape:
#    def __init__(self, width, height):
#       self.width = width
#       self.height = height

#    def __str__(self):
#       return f'Shape: width={self.width}, height={self.height}'

# shape1 = Shape(5, 3)
# print(shape1)

# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   def __init__(self, count, word):
      self.count = count
      self.word = word

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

