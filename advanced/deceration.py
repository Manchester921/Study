#-*- Coding:utf-8 -*-
"""
    decoration.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    时间装饰器  
    @author: Manchester
    @data: 2018-04-17 PM
"""

import math
import time


def deco(func):
    def sum(*args):
        starttime = time.time()
        func(*args)
        endtime = time.time()
        print("耗时:{0}".format(endtime-starttime))
    return sum

@deco
def func(a, b, c, fun):
    derta = b**2 - 4*a*c
    #print(derta)
    if a == 0:
        print('错误：a不能等于 0 ')
    elif derta >= 0:
        res1 = ( -b + fun(derta) ) / (2*a)
        res2 = ( -b - fun(derta) ) / (2*a)
        print('第一个解为:>%10f\n第二个解为:>%10f' % (res1,res2))
    else:
        print('此题无解')

if __name__=="__main__":
    a, b, c = map(int, input('请输入需要解的二元一次方程的a,b,c值(用空格分开):>').split())
    func(a, b, c, math.sqrt)
    #print(a, b, c)
    #print(type(a), type(b), type(c))
