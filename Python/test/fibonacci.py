#-*- coding:utf-8 -*-
"""
    fibonacci.py
    ~~~~~~~~~~~~~~~~
    斐波纳契数列的输出
    用斐波纳契数列计算黄金分隔数
"""

num = int(input("请输入需要输出的斐波纳契数列的项数:"))
a, b, c, count = 1, 1, 2, 0
while count < num:
    print('第%d项的斐波纳契数为：%d' %(count, a))
    a, b, count = b, a+b, count+1
while abs(a/b - b/c) > 0:
    a, b, c = b, c, b+c
print('黄金分割数为：',b/c)

