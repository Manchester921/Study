#-*- Coding:utf-8-*-
"""
    derivative.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    推导式 迭代器 生成器
    @author: Manchester
    @data: 2018-04-20 
"""


print('~'* 50)                       # 字典推导式
dictset1 = {'A': 1, 'B':2, 'C':3, 'D':3, 'E':5, 'F':6}
dict1 = { k for k in dictset1.values() }
print(dict1)
print(type(dict1))


print('~'* 50)                       # 列表推导式
dataset1 = list(range(10))
listIter = iter(dataset1)
print(listIter)
print(next(listIter))


print('~'* 50)                      # 生成器原型
dataset2 = []
def foo():
    for i in range(10):
        dataset2.append(i)
    return dataset2
lisrt = foo()
print(lisrt)

print('~'* 50)                      # 生成器
def foo2(): 
    for i in range(10):
        yield i
obj = foo2()
for item in obj:
    print(item)

print('~'* 50)
obj3 = ( i for i in range(10) if i % 2 == 2 )
print(type(obj3))
print(obj3)
for item2 in obj3:
    print(item2)

print('~'* 50)






