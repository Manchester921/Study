#-*- coding:utf-8 -*-
"""
    hanoi.py
    ~~~~~~~~~~~~~~~~~
    汉诺塔游戏的程序解决方法 改进版
"""

import time

n = int(input("请输入汉诺塔层数："))
count, x, y, z = 0,n,0,0

def move(V, num):
    global x, y, z
    if   V == 'X':
        x += num
    elif V == 'Y':
        y += num
    elif V == 'Z':
        z += num 
    return x, y, z 

def hanoi(n, X, Y, Z):
    global count, x, y, z
    if n == 1:
        x, y, z = move(X,-1)
        x, y, z = move(Z,1)    
        count += 1
        print(X,"-->",Z,"   ",x,y,z,"   ",count )
    else:
        hanoi(n-1,X,Z,Y)              #将前面n-1个盘子从x移动到y上面
        x, y, z = move(X,-1)
        x, y, z = move(Z,1)
        count += 1
        print(X, "-->",Z,"   ",x,y,z,"   ",count)        #将最底下的盘子从x移动到z上
        hanoi(n-1,Y,X,Z)              #将前面n-1个盘子从y移动到z上面

print('--> 开始计时.....')
print('#'*50)
print("移动方式   ",n,0,0)
startTime = time.time()               # 使用time()获取时间戳
hanoi(n,'X','Y','Z')
endTime = time.time()                 # 使用time()再获取时间戳
print('#'*50)
print('--> 游戏完成 结束计时.....')
msecs = (endTime - startTime)         # 计算两次时间差
print('--> 共耗时耗时：%f s' % msecs)  # 输出结果

