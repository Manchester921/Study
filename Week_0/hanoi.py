#-*- coding:utf-8 -*-
"""
    hanoi.py
    ~~~~~~~~~~~~~~~~~
    汉诺塔游戏的程序解决方法
"""


count = 0

def hanoi(n, X, Y, Z, x, y, z):
    global count
    if n == 1:
        if   X == 'X':
            x -= 1
        elif X == 'Y':
            y -= 1
        elif X == 'Z':
            z -= 1 
        if   Z == 'X':
            x += 1
        elif Z == 'Y':
            y += 1
        elif Z == 'Z':
            z += 1    
        count += 1
        print(X,"-->",Z,"  ",x,y,z,"  ",count)
    else:
        hanoi(n-1,X,Z,Y,x,y,z)              #将前面n-1个盘子从x移动到y上面
        if   X == 'X':
            x -= n
        elif X == 'Y':
            y -= n
        elif X == 'Z':
            z -= n
        if   Y == 'X':
            x += n-1
        elif Y == 'Y':
            y += n-1
        elif Y == 'Z':
            z += n-1
        if   Z == 'X':
            x += 1
        elif Z == 'Y':
            y += 1
        elif Z == 'Z':
            z += 1 
        count += 1
        print(X, "-->",Z,"  ",x,y,z,"  ",count)        #将最底下的盘子从x移动到z上
        
        hanoi(n-1,Y,X,Z,x,y,z)              #将前面n-1个盘子从y移动到z上面
        
n = int(input("请输入汉诺塔层数："))
print(n,0,0)
hanoi(n,'X','Y','Z',n,0,0)

