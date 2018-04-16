#-*- Coding:utf-8-*-
"""
    menu.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    简单的菜单选择操作  程序规范写作
    @author: Manchester
    @data: 2018-04-11 PM
"""

import getpass
import os
import random
import smtplib
import sys
import time
from email.header import Header
from email.mime.text import MIMEText


def clear():           #清屏函数
    os.system('cls')

"""
    函数作用：统一主界面与子菜单的样式
    函数输入：界面/菜单名称    菜单可以输入的几个选项
    函数输出：str 用户的选择
"""
def menu(menuName, menuContent):    
    clear()
    print(menuName)
    print("#"*50)
    print(menuContent)
    print("#"*50)
    choose = input('请选择：>')
    return choose

#~~~~~~~~~~~~~~~~~~~   注册登陆界面与其子界面    ~~~~~~~~~~~~~~~~~~~~~
"""
    函数功能：注册登陆界面 
    函数输出：str 目前登陆的用户名 ;  dic  新注册的用户及其信息
"""
def mainMenu(): 
        userInfoDate = userInfo
        while(True):    
            choice = menu('用户注册登陆菜单', '\t1.用户登陆\n\t2.用户注册\n\t3.退出系统')
            if choice == '1':
                account = logonMenu()
                if account:
                    return account, userInfoDate
            elif choice == '2':
                userInfoNew = loginMenu()
                userInfoDate.update(userInfoNew)
            elif choice == '3':
                if input('确定退出系统?(y/n):>').lower() == 'y':
                    getpass.getpass('再见~lalala~')
                    sys.exit(0)
            else:
                getpass.getpass('提示请输入1~3的数字\a')   

def logonMenu():              #用户登陆页面
    clear()
    print('用户登陆')
    print("#"*50)
    account = input('请输入账号：>')
    code = getpass.getpass('请输入密码：>')
    if account == '' or code == '':
        getpass.getpass('账号或密码不能为空\a')
        return            
    elif account in userInfo  and code == userInfo[account]['code']:  
        return account
    else :
        getpass.getpass('账号或密码错误\a')
        return

"""
    函数功能：发送验证邮件
    函数输入：str 随机的验证码;  str 账户名; str 要发送的邮件地址
    函数输出：bool 邮件发送成功与否
"""
def verifyCodeSeed(verifyCode, account, toAddr):
    fromAddr = 'testmail921@163.com'
    authorWord = 'testMail921'
    codeText = 'lalala网注册验证，您的验证码为%s' % verifyCode
    message = MIMEText(codeText, 'plain', 'utf-8')
    message['From'] = Header('My Test Mail')
    message['To'] = Header('Dear %s' % account, 'utf-8')
    message['Subject'] = Header('lalala网注册验证', 'utf-8')
    try:
        server = smtplib.SMTP('smtp.163.com',25)
        server.login(fromAddr, authorWord)
        server.sendmail(fromAddr, [toAddr], message.as_string())
        server.quit()
        return True
    except:
        return False

def loginMenu():              #用户注册页面
    userInfoEdit = {}
    while(True):
        clear()
        print('新用户注册')
        print('~'*50)
        account = input('登陆账号:>')

        code = getpass.getpass('登陆密码:>')
        code2 = getpass.getpass('确认密码:>')
        if code == code2:
            mail = input('请输入正确的验证邮箱:>') 
            verifyCode = str(random.randint(100000, 999999))
            #if verifyCodeSeed(verifyCode, account, mail):       #邮件发送验证码
            if '@' in mail:
                print('注册验证码邮件发送成功!')
                print(verifyCode)
                if verifyCode == input('请输入验证邮箱:>'):
                    print('验证成功！')
                    name = input('用户昵称:>')
                    gender = input('性别:>')
                    age = input('年龄:>')
                userInfoEdit[account] = {'code':code, 'name':name, 'gender':gender, 'age':age,}
                choose = input('是否继续输入(y/n):>')
                if choose.lower() != 'y':
                    return userInfoEdit
            else:
                getpass.getpass('[错误]请输入正确邮箱<回车继续>\a')

        else:
            getpass.getpass('[错误]两次密码不一致<回车继续>\a')

#~~~~~~~~~~~~~~~~~~~   主菜单界面与其子界面    ~~~~~~~~~~~~~~~~~~~~
"""
    函数功能：主菜单界面
    函数输出：str 用户注册的信息
"""
def mainMenuUser():
    goodsInfoDate = goodsInfo
    while(True):
        choice = menu('主菜单界面  欢迎%s' % userInfo[account]['name'],\
                 '\t1.用户管理\n\t2.报表管理\n\t3.录入商品信息\n\t4.显示全部商品\n\t5.退出登陆')
        if choice == '1':
            accountManage()
        elif choice == '2':
            reportManage()
        elif choice == '3':
            goodsInfoNew = goodsInput()
            goodsInfoDate.update(goodsInfoNew)
        elif choice == '4':
            goodsInfoDisplay()
        elif choice == '5':
            if input('确定退出登陆?(y/n):>').lower() == 'y':
                getpass.getpass('再见~%s~' % userInfo[account]['name'])
                return goodsInfoDate
        else:
            getpass.getpass('提示请输入1~5的数字\a')

def accountManage():            #用户管理子菜单的函数
    while(True):
        choice = menu('用户管理菜单', '\t1.添加用户\n\t2.删除用户\n\t3.退出用户管理菜单')
        if choice == '1':
            getpass.getpass('正在添加用户...')
        elif choice == '2':
            getpass.getpass('正在删除用户...')
        elif choice == '3':
            break            
        else:
            getpass.getpass('提示请输入1~3的数字\a')

def reportManage():             #报表管理子菜单的函数
    while(True):
        choice = menu('报表管理菜单', '\t1.生成报表\n\t2.导出报表\n\t3.退出报表管理菜单')
        if choice == '1':
            getpass.getpass('正在执行<生成报表>操作...')
        elif choice == '2':
            getpass.getpass('正在执行<导出报表>操作...')
        elif choice == '3':
            break
        else:
            getpass.getpass('提示：请输入1~3的数字\a')

"""
    函数功能：编辑/录入商品信息
    函数输出：dic 本次录取商品的信息
"""
def goodsInput():
    goodsInfoEdit = {}
    while(True):
        clear()
        print('编辑/录入商品信息')
        print('~'*50)
        goodsId = time.strftime('%Y%m%d%H%M%S',time.localtime())
        print('商品ID:>', goodsId)
        goodsNum = input('请输入商品编号:>')
        goodsName = input('请输入商品名称:>')
        goodsPrice = input('请输入商品价格:>')
        choose = input('是否继续输入(y/n):>')
        goodsInfoEdit[goodsNum] = [goodsId, goodsName, goodsPrice]
        if choose.lower() != 'y':
            return goodsInfoEdit

def goodsInfoDisplay():             #商品信息子菜单的函数
    clear()
    print('共有%s件商品' % len(goodsInfo))
    print('~'*50)
    for goods in goodsInfo:
        print('\n商品ID：%s\n' % goodsInfo[goods][0], '~'*50)
        print('商品编号：%s\n商品名称：%s\n商品价格：￥%s\n'\
               % (goods, goodsInfo[goods][1], goodsInfo[goods][2]) )
    getpass.getpass('提示:回车返回')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~   主函数入口   ~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    #读取基础信息
    userInfo = {'Manchester':{'code':'921', 'name':'lalala', 'gender':'男', 'age':'21',}}
    goodsInfo = {}
    
    while(True):
        #登陆注册主界面
        account, userInfoDate = mainMenu()
        userInfo.update(userInfoDate)
        #用户安全措施
        if account not in userInfo:
            getpass.getpass('[错误]未注册用户！')
            sys.exit(0)        
        #主菜单界面
        goodsInfoDate = mainMenuUser()
        userInfo.update(goodsInfoDate)
    pass
