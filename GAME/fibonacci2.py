#-*- coding:utf-8 -*-
"""
    fibonacci.py
    ~~~~~~~~~~~~~~~~
    斐波纳契数列的输出
    用斐波纳契数列计算黄金分隔数
"""


print('~'*50)                 # 常规方法
num = int(input("请输入需要输出的斐波纳契数列的项数:"))
a, b, count = 1, 1, 0
while count < num:
    print('第%d项的斐波纳契数为：%d' %(count+1, a))
    a, b, count = b, a+b, count+1


print('~'*50)                      # 列表追加法
fibs = [1, 1]
for i in range(num-2):
    fibs.append(fibs[-2] + fibs[-1]) 
print(fibs)


print('~'*50)                  # lambda 函数递归法
fib = lambda n : 1 if n<=2 else fib(n-1)+fib(n-2)
print(fib(num))


print('~'*50)                        # 函数递归法
def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
print(fibonacci(num))


print('~'*50)                         # 黄金分割数
a, b, c, count = 1, 1, 2, 1
while count <= num:
    print('第%d项的斐波纳契数为：%d' %(count, a))
    a, b, count = b, a+b, count+1
while abs(a/b - b/c) > 0:
    a, b, c = b, c, b+c
print('黄金分割数为：%.50f' % (b/c))



class Fibs:                          # 迭代器版。。
    def __init__ (self):  
        self.a =0  
        self.b =1  
    def __next__(self):  
        self.a , self.b = self.b, self.a+self.b  
        return self.a  
    def __iter__(self):  
        return self
fibs = Fibs()
for i in range(num):
    print(next(fibs) ,end=', ')