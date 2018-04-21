#-*- Coding:utf-8-*-
"""
    printUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    作业1/2:print基本函数应用
    @author: Manchester
    @data: 2018-04-09 AM
"""
import random
import time

if __name__ == '__main__':

    print('~'*50)

    pi = 3.141592653  
    print('%10.3f' % pi)      #字段宽10，精度3  
    print('%010.3f' % pi) #用0填充空白  
    #000003.142  
    print('%-10.3f' % pi) #左对齐  
    #3.142       
    print('%+f' % pi) #显示正负号  
    #+3.141593

    print('~'*50)

    for i in range(10):
        print(i, end = '' )
    for i in range(10):
        print(i, end = '', flush=True)    #flush end是在for结束后输出
    
    print('\n' + '~'*50)                  #逗号 有空格  与加号
    
    for i in range(25):
        print(' ' , end='>', flush=True)      
        time.sleep(0.02 * random.random() * i)

    print('\n'+'~'*50)
        
    name = input('请输入您的姓名：')
    if name == 'monster':
        print('我不和怪物说话')
    else:
        print('你好！%s' % name)

