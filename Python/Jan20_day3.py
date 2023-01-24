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
#Exception Handeling 
'''
try :

except :

else :

finally :
'''
'''
try:
    f = open("file.txt","w")
    a,b = [int(x) for x in input("Enter two numbers : ").split(" ")]
    c = a/b
    f.write(f"writing {c} into file")
except ZeroDivisionError:
    print("Error : b cant be 0")
'''
'''
try:
    name = input("enter your name ")
    f = open("file.txt", "r")
except IOError as ie:
    print("File not exist")
else:
    n = len(f.read())
    print("file has ", n, "lines")
'''
# Exception in function
'''
def avg(l):
    t=0
    for i in l:
        t+=i
    avg= t/len(l)
    return t, avg

try:
    t, a = avg([1,2,3,4,"p"])
    print(f"total = {t} , avg = {a}")
except TypeError as te:
    print(te)
except ZeroDivisionError as ze:
    print(ze)
'''
#Making user defined exception
'''
class MyException(Exception):
    def __init__(self, arg):
        self.arg = arg
        
def check(d):
    for k,v in d.items():
        print(k,v)
        if v<2000.0:
            raise MyException("Balance is 0")

b = {"Raj" : 4000, "Ramesh" : 3000, "mahesh" : 1000, "Ram": 400}
try :
    check(b)
except MyException as me:
    print(me)
'''  
#Logging the exception
'''
#Debug levels - 
critical 50
error 40
warning 30
info 20
debug 10
not set 0
''' 
'''
import logging
logging.basicConfig(filename = "file.log",level=logging.DEBUG)
logger = logging.getLogger("__name__")

try:
    a = int(input("Enter a number :"))
    b = int(input("Enter second number "))
    c = a/b
    logger.info("Done")  
except ZeroDivisionError as ze:
    logger.exception(ze)
'''

#Generators

'''def count(n):
    i = 1
    while i<n:
        yield i
        i+=1
for i in count(5):
    print(i)
'''
#Iterators
'''
class MyIterator:
    def __init__(self,l,h):
        self.l=l
        self.h=h

    def __iter__(self):
        return self

    def __next__(self):
        if self.l<=self.h:
            self.l+=1
            return self.l-1
        else:
            raise StopIteration

it=MyIterator(20,400)
for i in it:
    print(i)
'''

#Decorators
'''
def my_decorator(func):
    def inner(n1,n2):
        n = 10
        f = func(n1,n2)
        return 10+f
    return inner

@my_decorator
def func(n1,n2):
    return n1+n2

# n1 = int(input("Enter a number"))
# n2 = int(input("Enter second number"))
# print(func(n1,n2))
'''
'''
def my_decorator(func):
    def inner(n1,n2):
        n = 10
        f = func(n1,n2)
        return 10+f
    return inner

def doubleval(myfunc):
    def inner(a,b):
        f = myfunc(a,b)
        return f*2
    return inner

@doubleval
@my_decorator   
def myfunc(a,b):
    return a**b

print(myfunc(10,2))
'''

