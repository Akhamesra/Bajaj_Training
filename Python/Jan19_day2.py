import pdb
#Python Object Oriented programming
'''
class Emp:
    __x = 10000
    def __init__(self,eid,ename,esal=30000):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("EID\t Ename\t Esal")
        print(self.eid,"\t", self.ename,"\t", self.esal)

if __name__=='__main__':
    a = Emp("E01", "Akshit",50)
    a.display()
#    print(a.__x) -> It will give error because private memeber cant be accessed 
    print(a._Emp__x) # can access private member like this
'''
#Change class variable
'''
class Emp:
    x = 10000
    def __init__(self,eid,ename,esal=30000):
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        print("EID\t Ename\t Esal")
        print(self.eid,"\t", self.ename,"\t", self.esal)
    
    @classmethod
    def modify(cls,n):
        cls.x = n

    @staticmethod
    def static_demo(n):
        Emp.x = 2000


e1 = Emp("EO1","Askhit", 30000)
print(e1.x)
e1.static_demo(2000)
print(e1.x)
e2 = Emp("EO2", "Aryamaan", 50000)
print(e2.x)
'''

#args,kwargs
'''
def my_func(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(args,kwargs)
    for a in args:
        print(a,end=" ")
    print()
    for k,v in kwargs.items():
        print(k,v, end=" ")
    print()

my_func(1,2,3,4,5,x=4,y=6,z=10,a=11)
'''

#DEBUGGIN pdb
"""
import pdb
pdb.set_trace() -> add break point
next -> execute the current line and move to next line
step -> go into the function called at the current line
jump 5 -> jump to line number 5
"""
'''
 class Person:
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastname(self):
        return self.name.split()[-1]
    
    def give_raise(self,percent):
        self.pay = int(self.pay+(self.pay * percent/100))
    def __repr__(self):
        return "[Person: %s %s]" %(self.name,self.pay)

bob = Person("Bob Smith")
she = Person("She Jones", job = "dev", pay=100000)
bob.give_raise(20)
print(she.lastname(),"pay=",she.pay)
print(bob.__repr__())
'''

#__repr__
'''
import datetime
now = datetime.datetime.now()
print(now.__str__())
print(now.__repr__())
'''

#Operator Overloading
'''
class Book1:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self,other_ob):
        return self.pages + other_ob.pages

class Book2:
    def __init__(self,pages):
        self.pages = pages
    def __gt__(self,ob):
        return self.pages > ob.pages
    
b1 = Book1(100)
b2 = Book2(500)
print('Total Pages = ',b1+b2)

if b1>b2: #It will not work because > is overloaded only for b2 so we have to write b2>b1
    print("B2 has more pages")
else:
    print("B1 has more pages")

if b2>b1: #It will work
    print("B2 has more pages")
else:
    print("B1 has more pages")
'''

# re module
import re
'''
import re
s =  "car rat mat fat"
    #method 1
p = re.compile(r'm\w\w') 

    #method 2
r = re.search(r'm\w\w',s)
print(r.group())
'''
# s = "This; is the: 'core' python\'s book"
# r = re.split(r'\w+',s)
# print(r)

# s2 = "This is beautiful"
# r = re.sub(r'beautiful', r'ugly',s2) #substitue
# print(r)

# s3 = "an apple a day keeps the doctor away"
# r = re.findall(r'a[\w]*',s3)
# for w in r:
#     print(w)

#ASSIGNMENT
'''
From file.txt find all the email it contains
'''
'''
with open("file.txt","r") as f:
    text = f.read()
    r = re.findall(r'\w+@\w*+.\w*',text)
    for w in r:
        print(w)
'''

#ASSIGNMENT
'''
print dates in the string
'''
'''s = "Today is 2023/12/09. Next class will be from 6/10/2023"

r = re.findall(r'\d+/\d+/\d+',s)
for w in r:
    print(w)
'''
# url = r"https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv"

# from urllib.request import urlopen
# def read_data(url):
#     if url.startswith(('https:','https:','ftp:')):
#         return urlopen(url).read()
#     else:
#         print("Not valid url")

# s = read_data(url).decode('utf-8')
# print(s)
'''
url = r"https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv"

from urllib.request import urlopen

def read_data(url):
    if url.startswith(('http:','https:','ftp:')):
        return urlopen(url).read()  

    else:
        print('Not valid url')

s=read_data(url).decode('utf-8')
print(s)
'''

