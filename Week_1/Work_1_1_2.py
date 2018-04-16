#-*- Coding:utf-8-*-
"""
    print.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    作业1/2:print基本函数应用
    @author: Manchester
    @data: 2018-04-09 AM
"""

if __name__ == '__main__':
    name = input('请输入您的姓名：')
    if name == 'monster':
        print('我不和怪物说话')
    else:
        print('你好！%s' % name)
