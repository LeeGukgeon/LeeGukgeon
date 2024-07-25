# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

class Dog(Animal):
    sound = '멍멍'
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    sound = '야옹'
    def __init__(self,sound):
        self.sound = sound
    def meow(self):
        print('야옹!')

class Pet(Cat,Dog):
    def __init__(self):
        pass
    
    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        print(self.sound)
    
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다'


pet1 = Pet()

print(pet1)