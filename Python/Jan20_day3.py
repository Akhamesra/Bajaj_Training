#Inheritance
'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_stud_info(self):
        return self.name,self.age
    def set_stud_info(self,name,age):
        self.name = name
        self.age = age
    
class ScienceStudent(Student):
    def __init__(self, name, age):
        super().__init__(name, age)
    def get_sub(self):
        return "Science"

s = ScienceStudent("Ram", 20)
print(s.get_stud_info())
s.set_stud_info("Ragul", 21)
print(s.get_stud_info())
print(s.get_sub())
'''
#Multiclass Inheritance
'''
class Animal:
    def __init__(self,animal):
        self.animal = animal
        print(self.animal, "is an Animal")

class Mammal(Animal):
    def __init__(self,mname):
        print(mname,"is a warm blooded")
        super().__init__(mname)

class NonWingedMammal(Mammal):
    def __init__(self,nwmammal):
        print(nwmammal, "cant fly")
        super().__init__(nwmammal)

class NonMarineMammal(Mammal):
    def __init__(self,nmmammal):
        print(nmmammal, "can't swim")
        super().__init__(nmmammal)

class Dog(NonMarineMammal,NonWingedMammal):
    def __init__(self):
        print("Dog has four legs")
        super().__init__('Dog')

d = Dog()
print(Dog.mro())
'''
#Polymorphism
'''
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am cat, my name is {self.name} and my age is {self.age}")
    def speak(self):
        print("meow!")

class Dog :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am dog, my name is {self.name} and my age is {self.age}")
    def speak(self):
        print("bark!")
    
c1 = Cat("Meow", 5)
d1 = Dog("Jimmy", 10)

for animal in (c1,d1):
    animal.info()
    animal.speak()
'''

# Method overiding, Abstract function
'''
from math import pi
class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def fact(self):
        return "2D Shape"
    def __str__(self):
        return self.name

class Square(Shape):
    def __init__(self,length):
        super().__init__('Square')
        self.length = length
    def area(self):
        return self.length * self.length
    def fact(self):
        return "Each Angle is of 90 degree"

class Circle(Shape):
    def __init__(self,r):
        super().__init__("Circle")
        self.r = r
    def area(self):
        return pi*self.r*self.r
    
s1 = Square(4)
c1 = Circle(5.6)

print(s1)
print(s1.area())
print(s1.fact())

print(c1)
print(c1.area())
print(c1.fact())
'''
#Asbtract Class
'''
from abc import ABC, abstractclassmethod
class MyClass(ABC):
    @abstractclassmethod
    def calc(self,x):
        pass
class SubClass(MyClass):
    def calc(self,x):
        print("Square = ", x**2)

ob = SubClass()
ob.calc(15)
'''

