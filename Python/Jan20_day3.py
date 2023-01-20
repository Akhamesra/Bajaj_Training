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


