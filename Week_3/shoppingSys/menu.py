# -*- Coding:utf-8 -*-
"""
    shoppingSys.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    现购物系统应用
    @author: Manchester
    @data: 2018-04-29
"""

import getpass
import os
import random
import smtplib
import sys
import time
import json
from email.header import Header
from email.mime.text import MIMEText
import re
import requests
import urllib.request


class CustomerInfo():
    def __init__(self, account, dictInfo):
        self.__name = account
        self.__code = dictInfo['code']
        self.__money = dictInfo['money']
        self.__isSeller = False
        self.__info = dictInfo

    pass


# 由于时间有限，设计有些仓促，没有将自己发布的商品添加到这个类里面，故不能购买自己发布的商品

class ProductInfo():
    def __init__(self, pid, dictInfo):
        self.__id = pid
        self.__category = dictInfo['category']
        self.__name = dictInfo['name']
        self.__price = dictInfo['price']
        self.__number = dictInfo['number']
        self.__info = dictInfo
    pass



class OrderInfo():
    def __init__(self):
        self.ordersInfo = {}
        pass
    
    
    
    def addOrder(self, userInfo, booksInfo, num):
        orderInfo = {}
        orderInfo['sellName'] = booksInfo['name']
        orderInfo['buyName'] = userInfo['name']
        orderInfo['num'] = num
        orderInfo['address'] = userInfo['address']
        orderInfo['phone'] = userInfo['phone']
        orderInfo['price'] = booksInfo['price']
        orderInfo['info'] = {'userInfo':userInfo, 'booksInfo':booksInfo}
        oid = time.strftime('%Y%m%d%H%M%S', time.localtime()) + str(random.randint(10000, 99999))
        self.ordersInfo[oid] = orderInfo

    
    def showAll(self):
        if not self.ordersInfo:
            return False
        for pid in self.ordersInfo:
            OInfo = self.ordersInfo[pid]
            print('~'*50+'\n订单ID：%s\n商品名：%s\n买家名：%s\n商品价格：%s\n商品数量：%s\n地址：%s\n电话：%s\n'%\
                    (pid, OInfo['sellName'], OInfo['buyName'], OInfo['price'], OInfo['num'], OInfo['address'], OInfo['phone']) )
        return True

    def showOrder(self, goodsId):
        if goodsId in self.ordersInfo:
            pid = self.ordersInfo[goodsId]
            print('您输入的订单信息为：')
            print('~'*50+'\n订单ID：%s\n商品名：%s\n买家名：%s\n商品价格：%s\n商品数量：%s\n地址：%s\n电话：%s\n'%\
                    (goodsId, pid['sellName'], pid['buyName'], pid['price'], pid['num'], pid['address'], pid['phone']) )
            return True
        else:
            getpass.getpass('\t<错误>没有该订单')
            return False



    pass




class Menu():

    def __init__(self, userInfo, booksInfo):
        self.userInfo = userInfo
        self.booksInfo = booksInfo
        self.account = None
        self.addProductInfo = {}
        # 读取基础信息
        pass

    def clear(self):
        """清屏函数"""
        os.system('cls')


    """ 
        @name: menu
        @args: str 界面/菜单名称; str 菜单可以输入的几个选项
        @return: str 用户的选择
        @data: 2018-04-12 PM
    """
    def menu(self, menuName, menuContent):
        """统一主界面与子菜单的样式"""
        self.clear()
        print(menuName)
        print("#"*50)
        print(menuContent)
        print("#"*50)
        choose = input('请选择：>')
        return choose

    # ~~~~~~~~~~~~~~~~~~~   注册登陆界面与其子界面    ~~~~~~~~~~~~~~~~~~~~~


    """ 
        @name: mainMenu
        @args: None
        @return: str 目前登陆的用户名; dic 新注册的用户及其信息
        @data: 2018-04-12 PM
    """
    def mainMenu(self):
        """注册登陆界面"""
        self.count = 3
        while self.count > 0:
            choice = self.menu('用户注册登陆菜单', '\t1.用户登陆\n\t2.用户注册\n\t3.退出系统')
            if choice == '1':
                self.logonMenu()
                if self.account:
                    return
            elif choice == '2':
                self.loginMenu()
            elif choice == '3':
                if input('确定退出系统?(y/n):>').lower() == 'y':
                    getpass.getpass('再见~lalala~')
                    break
            else:
                getpass.getpass('提示请输入1~3的数字\a')
        sys.exit(0)


    """ 
        @name: logonMenu
        @args: None
        @return: str 登陆者的用户名
        @data: 2018-04-13 PM
    """
    def logonMenu(self):
        """用户登陆页面"""
        self.clear()
        print('用户登陆')
        print("#"*50)
        account = input('请输入账号：>')
        code = getpass.getpass('请输入密码：>')
        if account == '' or code == '':
            getpass.getpass('账号或密码不能为空\a')
        elif account in self.userInfo and code == self.userInfo[account]['code']:
            self.account = account
            self.userOrder = OrderInfo()
        else:
            self.count -= 1
            print('还剩%s次机会' % self.count)
            getpass.getpass('账号或密码错误\a')

                



    """ 
        @name: verifyCodeSeed
        @args: str 随机的验证码; str 账户名; str 要发送的邮件地址
        @return: bool 邮件发送成功与否
        @data: 2018-04-13 PM
    """
    def verifyCodeSeed(self, verifyCode, account, toAddr):
        """发送验证邮件"""
        fromAddr = 'testmail921@163.com'
        authorWord = 'testMail921'
        codeText = 'lalala网注册验证，您的验证码为%s' % verifyCode
        message = MIMEText(codeText, 'plain', 'utf-8')
        message['From'] = Header('My Test Mail')
        message['To'] = Header('Dear %s' % account, 'utf-8')
        message['Subject'] = Header('lalala网注册验证', 'utf-8')
        try:
            server = smtplib.SMTP('smtp.163.com', 25)
            server.login(fromAddr, authorWord)
            server.sendmail(fromAddr, [toAddr], message.as_string())
            server.quit()
            return True
        except:
            return False


    """ 
        @name: loginMenu
        @args: None
        @return: dic 新注册者的信息
        @data: 2018-04-12 PM
    """
    def loginMenu(self):
        """用户注册页面"""
        while 1:
            self.clear()
            print('新用户注册')
            print('~'*50)
            account = input('登陆账号:>')
            if account in self.userInfo:
                getpass.getpass('[错误]该账号已被注册<回车继续>\a')
                return
            code = getpass.getpass('登陆密码:>')
            code2 = getpass.getpass('确认密码:>')
            if code == code2:
                mail = input('请输入正确的验证邮箱:>')
                verifyCode = str(random.randint(100000, 999999))
                # if verifyCodeSeed(verifyCode, account, mail):       # 邮件发送验证码
                if '@' in mail:                                       # 测试使用
                    print('注册验证码邮件发送成功!')
                    print(verifyCode)
                    if verifyCode == input('请输入验证码:>'):
                        print('验证成功！')
                        name = input('用户昵称:>')
                        phone = input('手机号码:>')
                        address = input('家庭地址:>')
                        self.userInfo[account] = {'code': code, 'name': name, 'money':0,'address':address, 'phone':phone}
                        customer = CustomerInfo(account, self.userInfo[account])
                        customers[account] = customer
                        self.userInfoUpdate(self.userInfo)
                    if input('是否继续输入(y/n):>').lower() != 'y':
                        return
                else:
                    getpass.getpass('[错误]请输入正确邮箱<回车继续>\a')

            else:
                getpass.getpass('[错误]两次密码不一致<回车继续>\a')

    # ~~~~~~~~~~~~~~~~~~~   主菜单界面与其子界面    ~~~~~~~~~~~~~~~~~~~~


    """ 
        @name: mainMenuUser
        @args: None
        @return: None
        @data: 2018-04-11 PM
    """
    def mainMenuUser(self):
        """主菜单界面"""
        while(True):
            choice = self.menu('主菜单界面  欢迎%s' % self.userInfo[self.account]['name'],
                        '\t1.用户管理\n\t2.商品发布\n\t3.购买商品\n\t4.订单编辑\n\t5.退出登陆')
            if choice == '1':
                self.accountManage()
            elif choice == '2':
                self.addProduct()
            elif choice == '3':
                self.purchasBook()
            elif choice == '4':
                self.orederEdit()
            elif choice == '5':
                if input('确定退出登陆?(y/n):>').lower() == 'y':
                    getpass.getpass('再见~%s~' % self.userInfo[self.account]['name'])
                    self.account = None
                    return
            else:
                getpass.getpass('<提示>请输入1~5的数字\a')


    """ 
        @name: accountManage
        @args: None
        @return: None
        @data: 2018-04-11 PM
    """
    def accountManage(self):
        """用户管理子菜单的函数"""
        while(True):
            choice = self.menu('用户管理菜单', '\t1.修改密码\n\t2.用户充值\n\t3.退出用户管理菜单')
            if choice == '1':
                if  getpass.getpass('请输入旧密码:>') == self.userInfo[self.account]['code']:
                    codeNew = getpass.getpass('请输入新密码:>')
                    if codeNew == getpass.getpass('请确认新密码:>'):
                        self.userInfo[self.account]['code'] = codeNew
                        self.userInfoUpdate(self.userInfo)
                    else:
                        getpass.getpass('<提示>两次密码输入不一致！\a')
                else:
                    getpass.getpass('<提示>密码错误！\a')
            elif choice == '2':
                self.recharge()
            elif choice == '3':
                break
            else:
                getpass.getpass('<提示>请输入1~3的数字\a')



    """ 
        @name: recharge
        @args: None
        @return: None
        @data: 2018-04-11 PM
    """
    def recharge(self):
        """用户充值子菜单的函数"""
        try:
            money = int(input('请输入充值金额:>'))
            verifyCode = str(random.randint(100000, 999999))
            # if verifyCodeSeed(verifyCode, account, mail):       # 邮件发送验证码
            print('注册验证码邮件发送成功!')
            print(verifyCode)
            if verifyCode == input('请输入验证码:>'):
                self.userInfo[self.account]['money'] += money
                self.userInfoUpdate(self.userInfo)
                getpass.getpass('充值成功！')
            else:
                getpass.getpass('验证失败！')
                
        except ValueError:
            getpass.getpass('提示：请输入的数字\a')


    """ 
        @name: goodsInput
        @args: None
        @return: dic 本次录取商品的信息
        @data: 2018-05-05 PM
    """
    def orederEdit(self):
        """编辑订单信息"""

        self.clear()
        print('\t订单编辑子菜单\n'+'\n')
        if self.userOrder.showAll():
            while 1:
                orderId = input('请输入需要编辑的订单ID:>')
                if self.userOrder.showOrder(orderId):
                    while 1:
                        orderInfoName = input('请输入需要编辑的订单信息:>')
                        if orderInfoName =='地址':
                            reOrder = input('请输入新信息:>')
                            self.userOrder.ordersInfo[orderId]['address'] = reOrder
                        elif orderInfoName =='电话':
                            reOrder = input('请输入新信息:>')
                            self.userOrder.ordersInfo[orderId]['phone'] = reOrder
                        else:
                            getpass.getpass('<输入有误>请输入“电话”或“地址”')
                        if input('是否继续编辑信息(y/n)').lower() != 'y':
                            return 
                if input('是否继续编辑其他订单(y/n)').lower() != 'y':
                    return
        else:
            getpass.getpass('当前没有订单')


    
    def addProduct(self):
        while 1:
            self.clear()
            print('编辑/录入商品信息\n'+'~'*50)
            category = input('请输入商品类别:>')
            pid = category + input('请输入商品编号:>')
            name = input('请输入商品名称:>')
            price = input('请输入商品价格:>')
            num = input('请输入商品存量:>')
            sellname = self.account
            self.addProductInfo[pid] = {'category':category, 'name':name, 'price':price, 'num':num, 'sellname':sellname }
            choose = input('是否继续输入(y/n):>')
            if choose.lower() != 'y':
                return 


            





    """ 
        @name: goodsInfoDisplay
        @args: None
        @return: None
        @data: 2018-04-11 PM
    """
    def purchasBook(self):
        """商品购买子菜单的函数"""
        self.bookInfo()
        while 1:
            proId = input('\n\n请输入需要购买的书本编号:>')
            if proId in self.booksInfo :
                print('您选择的是：%s\n这本书的价钱为：%s\n当前账户余额为：%s元' \
                        %(self.booksInfo[proId]['name'], self.booksInfo[proId]['price'],self.userInfo[self.account]['money']))
                try:
                    num = int(input('请输入购买数量:>'))
                except ValueError:
                    print('<错误>输入不为数字(默认为1)')
                if self.booksInfo[proId]['price']*num < self.userInfo[self.account]['money']:
                    if input('确定购买(y/n)?') == 'y':
                        self.userInfo[self.account]['money'] -= self.booksInfo[proId]['price']*num
                        self.userOrder.addOrder(self.userInfo[self.account], self.booksInfo[proId], num)
                        getpass.getpass('购买成功！当前账户余额为：%s元'%self.userInfo[self.account]['money'])

                    else:
                        getpass.getpass('<购买失败>未支付')
                else:
                    getpass.getpass('<购买失败>账户余额不足')
            else:
                getpass.getpass('<错误>请输入正确书本编号')  

            if input('是否继续购买(y/n):>') != 'y':
                break





    """ 
        @name: userInfoUpdate
        @args: dict
        @return: None
        @data: 2018-05-02 PM
    """
    def userInfoUpdate(self, userInfo):
        '''用户信息更新'''
        with open(filePath, 'w', encoding='utf8') as fp:
            json.dump(userInfo, fp, ensure_ascii=False)



    def bookInfo(self):
        self.clear()
        
        url = 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10005-1#comfort'
        headers ={'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}

        regExp = re.compile(r'[\s\n]{2,}')
        regItems = re.compile(r'<ul class="clearfix">(.*?)</ul>')
        regItem = re.compile(r'<div class="p-detail">(.*?)</div>')
        regTitle = re.compile(r'class="p-name">(.*?)</a>')
        regAuthor = re.compile(r'<dd>.*?<a.*?>(.*?)</a>')
        # regPrice = re.compile(r'<dd><em.*?>(.*?)</em>')

        response = requests.get(url, headers=headers)
        response.encoding = 'GB2312'
        content = response.text
        blockCode = regExp.sub('', content)
        lstItems = regItems.findall(blockCode)[0]
        lstItem = regItem.findall(lstItems)

        books = {}
        tid = 10000
        print('\t书本销售排行榜\n\t共有%s本书\n\n' % len(lstItem))

        for i in lstItem:
            lstTitle = regTitle.findall(i)[0].replace('\u3000', ' ')
            lstAuthor = regAuthor.findall(i)[0]
            lstPublish = regAuthor.findall(i)[1]
            price = random.randint(20,200)     # 网上数据爬不了 不能得到真实的数据  故读取每次价钱会变
            number = random.randint(20,200)
            tid += 1
            pid = 'book' + str(tid)
            self.booksInfo[pid] = {'category':'book', 'name':lstTitle, 'price':price,\
                     'number':number, 'author':lstAuthor,  'publish':lstPublish,   }
            book = ProductInfo(pid, self.booksInfo[pid])
            books[pid] = book
            print('~'*50,'\n编  号：%s\n书  名：%s\n作  者：%s\n出版社：%s\n价  格：%s\n库  存：%s\n'\
                % (pid, lstTitle,lstAuthor, lstPublish, price, number ))

        if self.addProductInfo:
            for pid in self.addProductInfo:
                PInfo = self.addProductInfo[pid]
                print('~'*50+ '\n编  号：%s\n商品名：%s\n卖家名：%s\n价  格：%s\n库  存：%s\n'\
                        % (pid, PInfo['name'], PInfo['sellname'], PInfo['price'], PInfo['num']))








# ~~~~~~~~~~~~~~~~~~~~~~~~~~~   主函数入口   ~~~~~~~~~~~~~~~~~~~~~~~~~~~





if __name__ == '__main__':

    userInfo = {'Manchester': {'code': '921','name': 'lalala', 'money':1000, 'address':'武汉市洪山区光谷软件园', 'phone':'13722223333'}}
    booksInfo = {}
    customers = {}
    fileDir = R'.\files'
    if not os.path.exists(fileDir): os.mkdir(fileDir)
    filePath = fileDir + os.sep + 'userInfo.json '   

    try:
        with open(filePath, 'r', encoding='utf8') as fp:
            json.load(fp).update(userInfo)
    except FileNotFoundError:
        with open(filePath, 'w', encoding='utf8') as fp:
            json.dump(userInfo, fp, ensure_ascii=False)

        
    while(True):
        # 登陆注册主界面
        menu = Menu(userInfo, booksInfo)
        menu.mainMenu()
        
        # 主菜单界面
        menu.mainMenuUser()
        

    pass
