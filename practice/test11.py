class Animal:
    def __init__(self):
        print('Animal')

class Dog(Animal):
    def __init__(self):
        print('Dog')
        super().__init__()

class Cat(Animal):
    def __init__(self):
        print('Cat')
        super().__init__()

class Pet(Dog,Cat):
    def __init__(self):
        print('Pet')
        super().__init__()

pet = Pet()