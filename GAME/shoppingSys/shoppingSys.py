# -*- Coding:utf-8 -*-
"""
    shoppingSys.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    现购物系统应用
    @author: Manchester
    @data: 2018-04-29
"""

import getpass
import json
import os
import random
import re
import smtplib
import sys
import time
import urllib.request
from email.header import Header
from email.mime.text import MIMEText

import requests


class CustomerInfo():
    def __init__(self, account, dictInfo):
        self.__name = account
        self.__code = dictInfo['code']
        self.__money = dictInfo['money']
        self.__isSeller = False
        self.__info = dictInfo



    pass


class ProductInfo():
    def __init__(self):
        self.productsInfo = {}
        self.bookInfo()

        pass

    """ 
        @name: addProduct
        @args: str dict
        @return: None
        @data: 2018-05-07 PM
    """
    def addProduct(self, pid, dictInfo):
        """增加商品信息"""
        productInfo = {}
        if pid not in self.productsInfo:
            productInfo['name'] = dictInfo['name']
            productInfo['category'] = dictInfo['category']
            productInfo['sellname'] = dictInfo['sellname']
            productInfo['price'] = dictInfo['price']
            productInfo['num'] = dictInfo['num']
            self.productsInfo[pid] = productInfo
        else:
            getpass.getpass('<错误>该商品编号已存在')

    """ 
        @name: editProInfo
        @args: str str str/int
        @return: None
        @data: 2018-05-07 PM
    """
    def editProInfo(self, pid, oldInfoName, newInfo):
        """编辑商品信息"""
        self.productsInfo[pid][oldInfoName] = newInfo

    """ 
        @name: showAll
        @args: None
        @return: None
        @data: 2018-05-07 PM
    """
    def showAll(self):
        """ 展示全部商品信息 """
        for pid in self.productsInfo:
            PInfo = self.productsInfo[pid]
            print('~'*50 + '\n编  号：%s\n商品名：%s\n类  别：%s\n卖家名：%s\n价  格：%s\n库  存：%s\n'
                  % (pid, PInfo['name'], PInfo['category'], PInfo['sellname'], PInfo['price'], PInfo['num']))

    """ 
        @name: bookInfo
        @args: None
        @return: None
        @data: 2018-05-05 PM
    """
    def bookInfo(self):
        """网上爬取书本信息"""
        url = 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10005-1#comfort'
        headers = {'User-Agent': 'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}

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

        tid = 10000
        for i in lstItem:
            lstTitle = regTitle.findall(i)[0].replace('\u3000', ' ')
            lstAuthor = regAuthor.findall(i)[0]
            lstPublish = regAuthor.findall(i)[1]
            price = random.randint(20, 200)     # 网上数据爬不了 不能得到真实的数据
            num = random.randint(20, 200)
            tid += 1
            pid = 'book' + str(tid)
            bookInfo = {'category': 'book', 'name': lstTitle, 'price': price,
                        'num': num, 'sellname': '%s / %s' % (lstAuthor, lstPublish)}
            self.addProduct(pid, bookInfo)


class OrderInfo():
    def __init__(self):
        self.ordersInfo = {}
        pass

    """ 
        @name: addOrder
        @args: dict dict int
        @return: bool
        @data: 2018-05-05 PM
    """
    def addOrder(self, userInfo, booksInfo, num):
        """增加订单信息"""
        orderInfo = {}
        orderInfo['sellName'] = booksInfo['name']
        orderInfo['buyName'] = userInfo['name']
        orderInfo['num'] = num
        orderInfo['address'] = userInfo['address']
        orderInfo['phone'] = userInfo['phone']
        orderInfo['price'] = booksInfo['price']
        orderInfo['info'] = {'userInfo': userInfo, 'booksInfo': booksInfo}
        oid = time.strftime('%Y%m%d%H%M%S', time.localtime()) + str(random.randint(10000, 99999))
        self.ordersInfo[oid] = orderInfo

    """ 
        @name: showAll
        @args: None
        @return: bool
        @data: 2018-05-05 PM
    """
    def showAll(self):
        """ 展示全部订单信息 """
        if not self.ordersInfo:
            return False
        for pid in self.ordersInfo:
            OInfo = self.ordersInfo[pid]
            print('~'*50+'\n订单ID：%s\n商品名：%s\n买家名：%s\n商品价格：%s\n商品数量：%s\n地址：%s\n电话：%s\n' %
                  (pid, OInfo['sellName'], OInfo['buyName'], OInfo['price'], OInfo['num'], OInfo['address'], OInfo['phone']))
        return True

    """ 
        @name: showOrder
        @args: str 需要显示的商品ID
        @return: bool
        @data: 2018-05-05 PM
    """
    def showOrder(self, goodsId):
        """ 展示订单信息 """
        if goodsId in self.ordersInfo:
            pid = self.ordersInfo[goodsId]
            print('您输入的订单信息为：')
            print('~'*50+'\n订单ID：%s\n商品名：%s\n买家名：%s\n商品价格：%s\n商品数量：%s\n地址：%s\n电话：%s\n' %
                  (goodsId, pid['sellName'], pid['buyName'], pid['price'], pid['num'], pid['address'], pid['phone']))
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
        self.productsInfo = ProductInfo()
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
        @return: None
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
        @return: None
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
                        self.userInfo[account] = {
                            'code': code, 'name': name, 'money': 0, 'address': address, 'phone': phone}
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
                self.addProductMenu()
            elif choice == '3':
                self.purchasBook()
            elif choice == '4':
                self.orederEdit()
            elif choice == '5':
                if input('确定退出登陆?(y/n):>').lower() == 'y':
                    getpass.getpass('再见~%s~' %
                                    self.userInfo[self.account]['name'])
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
                if getpass.getpass('请输入旧密码:>') == self.userInfo[self.account]['code']:
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
        @data: 2018-04-28 PM
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
        @name: orederEdit
        @args: None
        @return: None
        @data: 2018-05-07 PM
    """
    def orederEdit(self):
        """编辑订单信息"""
        self.clear()
        print('\t订单编辑子菜单\n'+'\n')
        if self.userOrder.ordersInfo:
            self.userOrder.showAll()
            while 1:
                orderId = input('请输入需要编辑的订单ID:>')
                if self.userOrder.showOrder(orderId):
                    while 1:
                        orderInfoName = input('请输入需要编辑的订单信息:>')
                        if orderInfoName == '地址':
                            reOrder = input('请输入新信息:>')
                            self.userOrder.ordersInfo[orderId]['address'] = reOrder
                        elif orderInfoName == '电话':
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

    """ 
        @name: addProductMenu
        @args: None
        @return: None
        @data: 2018-05-05 PM
    """
    def addProductMenu(self):
        while 1:
            self.clear()
            print('编辑/录入商品信息\n'+'~'*50)
            category = input('请输入商品类别:>')
            pid = category + input('请输入商品编号:>')
            name = input('请输入商品名称:>')
            while 1:
                try:
                    price = int(input('请输入商品价格:>'))
                    num = int(input('请输入商品存量:>'))
                    break
                except TypeError:
                    getpass.getpass('<错误>请输入数字')
            sellname = self.account
            productsInfo = {'category': category, 'name': name,
                            'price': price, 'num': num, 'sellname': sellname}
            self.productsInfo.addProduct(pid, productsInfo)
            if input('是否继续输入(y/n):>').lower() != 'y':
                return

    """ 
        @name: purchasBook
        @args: None
        @return: None
        @data: 2018-05-05 PM
    """
    def purchasBook(self):
        """商品购买子菜单的函数"""
        self.clear()
        psInfo = self.productsInfo.productsInfo
        print('\t商品销售子菜单\n\t共有%s件商品\n\n' % len(psInfo))
        self.productsInfo.showAll()
        while 1:
            proId = input('\n\n请输入需要购买的商品编号:>')
            if proId in psInfo:
                pInfo = psInfo[proId]
                accInfo = self.userInfo[self.account]
                print('您选择的是：%s\n这件商品的价钱为：%s\n当前账户余额为：%s元'
                      % (pInfo['name'], pInfo['price'], accInfo['money']))
                while 1:
                    try:
                        num = int(input('请输入购买数量:>'))
                        if pInfo['num'] - num < 0:
                            getpass.getpass('<购买失败>库存不足')
                            return
                        elif num <= 0:
                            getpass.getpass('请输入大于零的整数')
                        else:
                            break
                    except ValueError:
                        print('<错误>输入不为数字')
                if pInfo['price']*num < accInfo['money']:
                    if input('确定购买(y/n)?') == 'y':
                        accInfo['money'] -= pInfo['price']*num
                        pInfo['num'] -= num
                        self.productsInfo.editProInfo(proId, 'num', pInfo['num'])
                        self.userOrder.addOrder(accInfo, pInfo, num)
                        self.userInfo[self.account]['money'] = accInfo['money']
                        self.userInfoUpdate(self.userInfo)
                        getpass.getpass('购买成功！当前账户余额为：%s元' % accInfo['money'])

                    else:
                        getpass.getpass('<购买失败>未支付')
                else:
                    getpass.getpass('<购买失败>账户余额不足')
            else:
                getpass.getpass('<错误>请输入正确的商品编号')

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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~   主函数入口   ~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == '__main__':

    print('数据初始化中...')

    userInfo = {'Manchester': {'code': '921', 'name': 'lalala','money': 1000, 
                                'address': '武汉市洪山区光谷软件园', 'phone': '13722223333'}}
    booksInfo = {}
    customers = {}
    fileDir = R'.\files'
    if not os.path.exists(fileDir):
        os.mkdir(fileDir)
    filePath = fileDir + os.sep + 'userInfo.json '

    try:
        with open(filePath, 'r', encoding='utf8') as fp:
            userInfo = json.load(fp)
            userInfo.update(userInfo)
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
