#-*- coding:utf-8 -*-
"""
    Josephus_problem.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    1、约瑟夫问题：  
            问题：N个人坐一圈，从第一个人开始123依次报数，第三个人出列
            输出：出列顺序
    2、约瑟夫问题加强版：
            问题：编号1~N的N个人坐一圈，每人有可以自由输入的密码，开始一
        人密码为报数上限，报数到该数出列，并将出列的人的密码作
        为新的上限值
            输出：出列顺序与密码
"""

import random

print('约瑟夫问题加强版：')
print('#'*50)
N = int(input('请输入总人数：'))
U = int(input('请输入随机密码值的上限：'))
print(N,'个人的随机密码为：')
code = []
for i in list(range(U)):
    code.append(random.randrange(1,U))

print(code)
print(list(range(1,N+1)))
print('#'*50)


[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#code%len(l)
# for i in l[0:int(code[1]%len(l))]:
#     l.append(i)
# print(l)


l = list(range(1,N+1))
def cir(l,i,die):
    if i == N+1:
        return l[0]
    else:
        #print('  第',die,'个人死亡', end = '  ')
        print(l[die%len(l)-1], '死亡', end = '  ')
        print('他的密码为：',code[l[die%len(l)-1]-1])

        die = code[l[die%len(l)-1]-1]
        #print(die, end = '')
        for j in l[0:die-1]:
            l.append(j)
        del l[0:die]
        for j in code[0:die-1]:
            code.append(j)
        del code[0:die]



        print('剩下的人数为：',len(l))
        print(l)
        print(code)


        #print(' --> %d' % l[die-1], end = '')



        return cir(l,i+1,die)
cir(l,1,1)







# print('约瑟夫问题：')
# print('#'*50)
# N = int(input('请输入总人数：'))
# l = list(range(1,N+1))
# def cir(l,i):
#     if i == N+1:
#         return l
#     else:
#         l.append(l[0])
#         l.append(l[1])
#         print(' --> %d' % l[2], end = '')
#         del l[0:3]
#         return cir(l,i+1)
# cir(l,1) 
