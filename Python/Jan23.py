'''import re
with open("LICENSE_PYTHON.txt","r") as f:
    text = f.read().lower().split(" ")
    text2 = [] 
    for te in text:
        text2.append(re.findall(r'\b\w*\b',te))
    text2 = text
    print(text2)
    # d = {}
    # for i in set(text):

    #     val = text.count(i)
    #     if val in d:
    #         d[val].append(i)
    #     else:
    #         d[val] = [i]
    # print(d)

import re
with open("LICENSE_PYTHON.txt","r") as f:
    text = f.read().lower().split(" ")
    bow = dict()
    for word in text:
        count = text.count(word)
        li = bow.setdefault(count,set())
        li.add(word)
    print(bow)
 
'''
'''import copy
l1 = [1,2,3,['A','B']]
l2 = 
l2[-1].append('C')
print(l1)
print(l2)
'''

'''
l = ['Python', 'C', 'Java', 'C++']
print(sorted(l,key=len))'''

'''
l = [(1,2,3), (4,8,1), (2,4,5), (3,6,9)]
print(sorted(l,key=lambda x: x[1]))
'''

'''
import os
path = "/Users/akshitkhamesra/Desktop/Training/Python/"
ls = os.listdir(path)
print(sorted(ls,key =  lambda x:os.path.getsize(path+x)))
'''
'''
from itertools import combinations
l = text.split()
perm = combinations(l,2)
for i in list(perm):
    print(i)
'''
'''
text = "Python is easy to learn"
num = int(input("Enter a number : "))
k = len(text.split())
l = []
for i in range(k-num+1):
    s = [text.split()[j] for j in range(i,i+num)]
    l.append(s)
print(l)
'''

'''
text = "Python is easy to learn"
text = text.split()
n = 2
print(list(zip(*[text[i:] for i in range(n)])))
'''

'''
import copy
l1 = [1,2,3,4,[9,8,7],(5,6,7)]
l2=  copy.deepcopy(l1)
print(l2[-3]is l1[-3])
'''
'''s = "Python29@#8496"
l = [int(x) for x in s if x.isnumeric()]
print(sum(l)/len(l))
'''


