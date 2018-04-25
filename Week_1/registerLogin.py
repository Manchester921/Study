#-*- Coding:utf-8 -*-
"""
    registerLogin.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    函数编程实现用户注册及登录验证
    @author: Manchester
    @data: 2018-04-20 PM
"""

import os
import sys
import getpass

""" 
    @name: menu()
    @args: None
    @return: None
    @data: 2018-04-20 PM
"""
def menu():
    '''主菜单界面'''
    os.system('cls')
    print('\n\t主菜单\n' + '~'*50 + '\n\t1.用户注册\n\t2.用户登陆\n\t3.退出系统\n' + '~'*50)
    choice = input('请输入您的选择:>')
    if choice == '1':
        register()
    elif choice == '2':
        if login():
            getpass.getpass('登陆成功')
    elif choice == '3':
        if input('确认退出？(y/n):>\a') == 'y':
            sys.exit()

""" 
    @name: isBlank
    @args: str 需要输入的内容主题, bool 是否显示输入, bool 是否有限制输入次数
    @return: str
    @data: 2018-04-20 PM
"""
def isBlank(inputWord, isPass = False, protect = False):
    '''验证是否为空并返回控制台的输入'''
    count = 3
    while 1:
        if isPass:
            word = getpass.getpass('请输入%s:>' % inputWord)
        else:
            word = input('请输入%s:>' % inputWord)
        if word == '':
            getpass.getpass('[提示]%s不能为空！' % inputWord)
        else:
            return word
        if protect:
            count -= 1 
            getpass.getpass('您还有%s次登陆机会' % count)
        if count == 0:
            sys.exit()

""" 
    @name: register()
    @args: None
    @return: bool
    @data: 2018-04-20 PM
"""
def register():
    '''用户注册界面'''
    global userInfo
    os.system('cls')
    print('\n\t用户注册页面\n' + '~'*50)
    acccount = isBlank('账号')
    code = isBlank('密码', isPass=True)
    if code != getpass.getpass('请确认密码:>'):
        getpass.getpass('[错误]两次密码不一样！')
        return False
    else:
        userInfo[acccount] = code
        return True

""" 
    @name: login()
    @args: None
    @return: bool
    @data: 2018-04-20 PM
"""
def login():
    '''用户登陆界面'''
    print('\n\t用户登陆页面\n' + '~'*50)
    acccount = isBlank('账号')
    if userInfo[acccount] == isBlank('密码', isPass=True, protect=True):
        return True
    else:
        return False

#主函数入口
if __name__ == '__main__':
    userInfo = {}
    while 1:
        menu()
