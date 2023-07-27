# # ws_8_1.py
# # 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
       Animal.num_of_animal += 1
    

# class Dog(Animal):
#     pass


# class Cat(Animal):
#     pass


# class Pet(Dog, Cat):
#    @classmethod
#    def access_num_of_animal(cls):
#        return f'동물의 수는 {cls.num_of_animal}마리 입니다.'

# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())


class Dog(Animal):
    # 클래스 속성 sound
    sound = "멍멍"


class Cat(Animal):
    # 클래스 속성 sound
    sound = "야옹"


class Pet(Dog, Cat):

    def __str__(self):
       return f'애완동물은 {self.sound} 소리를 냅니다.'
    
    @classmethod
    def __str__(cls):
       return f'애완동물은 {cls.sound} 소리를 냅니다.'

pet1 = Pet()
print(pet1)

class Pet(Cat, Dog):

    # 아래 인스턴스 메서드 생략해도 가능
    def __str__(self):
       return f'애완동물은 {self.sound} 소리를 냅니다.'
    
    # 클래스 속성(변수) 사용하기 위해 클래스 메서드 호출
    # 오버라이딩은 부모클래스의 메서드를 자식 클래스에서 재정의 하여 사용하는 것
    @classmethod
    def __str__(cls): 
       return f'애완동물은 {cls.sound} 소리를 냅니다.'

pet1 = Pet()
print(pet1)