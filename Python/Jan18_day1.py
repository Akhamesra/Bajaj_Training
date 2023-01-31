#ASSIGNMENT
'''
Q.)
Print the pattern
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
'''
x=int(input())
l = x-1
for n in range(0,x):
    for j in range(0,l):
        print(end=" ")
    l = l-1
    for b in range(0,n+1):
        print("* ",end="")
    print()
'''


'''
Q.)
To make the series
A
B C
D E F
'''
'''
n = int(input())
k = 1
for i in range(1,n):
    for j in range(i):
        print(chr(ord('A') - 1 + k),end = " ")
        k+=1
    print()
'''

#Docstring
"""
def my_function():
    '''This is my function and this is the description.'''
    return None
print(my_function.__doc__)
"""

#String slicing
'''
s = "I am learning python"
print(s[5:10])
print(s[5:10:3])
print(s[:3:-1])
'''

#String Split
'''
l = "xyz:345:21/6/2023"
s = l.split(":")
print(s)
'''

#Finding Index of a string
'''
s = "I am learning python"
print(s.find("py")) #gives starting index and if not found gives -1
print(s.index("py")) #gives starting index but if not found gives error
print(s.find("a",3,10))
'''

#Joining strings
'''
l = ["hello", "world"]
j = " ".join(l)
print(j)
'''

#Printing format
'''
print("1.){:5d}".format(12))
print("2.){:2d}".format(1234))
print("3.){:8.3f}".format(12.2346))
print("4.){:05d}".format(12))
print("5.){:08.3f}".format(12.2346))
print("6.){:^10.3f}".format(12.2346))
print("7.){:<05d}".format(12))
print("8.){:>08.13f}".format(12.2346))
print("9.){:=8.3f}".format(-12.2346))
print("Hello {} your balance is {}".format("Kapil",4563))
'''

#ASSIGNMENT
'''
Count number of occurances of each char in string
s = "I am learning Python"
'''
'''
s="i am learning python"
l = {}
for a in s:
    if a not in l:
        l[a] = 1
    else:
        l[a] +=1
print(l)
'''


# List functions
'''L = []
L.reverse()
L.pop()
L.index()
L.find()
L.count()
L.remove(10)
del L[2]
del L
L.clear()
L.insert(10,2)'''


# Tuple functions
'''T = ()
T = tuple()
T.count()
T.index()
T=(1,)'''

# Dictionary functions
'''
D = {}
D = dict()
D["Red"] = "Apple"
D = {"Red":"Apple", "Yellow":"Banana"}
D["Red"]
D.get("Red","empty")
for k in D:
    print(k,D[k])
for k in D.key():
    print(k,D[k])
print(sorted(D))
print(sorted(D.keys()))
print(sorted(D.values()))
l1 = ["India", "China", "SriLanka"]
l2 = ["Pune", "Beiging", "Colombo"]
print(dict(list(zip(l1,l2))))

'''
#Dict
'''
people = {1:{'Name':'John', 'Age':'22', 'Sex':'M'}, 2:{'Name':'Akshit', 'Age':'23', 'Sex':'M'}}
for p in people:
    print(p)
    for x in people[p]:
        print(x+':'+people[p][x])
'''

#Sets
'''s = set()
s1 = {1,2,3,3,2,1,6,7,8}
s2 = {1,2,10,11,2,3,8}
s.add(10)
print(s1)
print(s2)
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))'''


#List errors
'''
def my_function(my_list):
    my_list.append(100)

l = [1,2,3,4]
print(l)
my_function(l)
print(l)'''


#Factorial
'''
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(3))
'''

#String reversal
'''
s = 'Akshit'
rs = s[::-1]
print(rs)
'''

#Lambda Function
'''
x = lambda x,y : x+y
L = [1,2,3,4]
L = list(map(lambda x:x**3,L))
print(L)
L = list(filter(lambda x:x%2==0,L))
print(L)
from functools import reduce
L = reduce(lambda x,y:x+y,L)
print(L)
'''

#File Handling
'''
f = open(filename,mode)

f=open("/home/xyz/test.txt", "w")
f.write("this is my file")
f.write("second line")
f.close()
'''

#Open a file and edit its 4th and 5th line
'''
with open("test.txt", "r") as f:
    line = f.readline()
    line = f.red()
    line = f.read(10)
    line = f.readlines()
'''
'''
with open("file.txt","r") as f:
    l = []
    for line in f:
        l.append(line)
    l[3] = "Changed line\n"
    l[4] = "Changed line 2\n"

f = open("refile.txt","w")
for j in l:
    f.write(j)
f.close()
'''

#Importing class from other file
'''
import Jan19_day2 as e
a = e.Emp("1","Don",50)
a.display()
'''

