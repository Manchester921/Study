# -*- Coding:utf-8 -*-
"""
    ElectronicCoupon.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    面向对象编程电子优惠券申领
    @author: Manchester
    @data: 2018-04-20 PM
"""

import time
import getpass
import random


class ElectronicCoupon():

    def __init__(self):
        self.__ecid = None
        self.__ecprice = None
        self.__validity = None
        self.__passcode = None

    def __str__(self):
        print('[抵卷编号:%s, 抵卷面值:%s, 有效期:%s, 领取码:%s]'
              % (self.__ecid, self.__ecprice, self.__validity, self.__passcode))
        return ''

    @property
    def ecid(self):
        return self.__ecid

    @ecid.getter
    def ecid(self):
        return self.__ecid

    @ecid.setter
    def ecid(self, value):
        self.__ecid = value
        pass

    @property
    def ecprice(self):
        return self.__ecprice

    @ecprice.getter
    def ecprice(self):
        return self.__ecprice

    @ecprice.setter
    def ecprice(self, value):
        self.__ecprice = value
        pass

    @property
    def validity(self):
        return self.__validity

    @validity.getter
    def validity(self):
        return self.__validity

    @validity.setter
    def validity(self, value):
        self.__validity = value
        pass

    @property
    def passcode(self):
        return self.__passcode

    @passcode.getter
    def passcode(self):
        return self.__passcode

    @passcode.setter
    def passcode(self, value):
        self.__passcode = value
        pass


""" 
    @name: isBlank
    @args: str 需要输入的内容主题
    @return: int
    @data: 2018-04-20 PM
"""
def isBlank(inputWord):
    '''验证是否为空并返回控制台的输入'''
    while 1:
        try:
            word = int(input('请输入%s:>' % inputWord))
            if word == '':
                getpass.getpass('[提示]抵卷面值不能为空！')
            else:
                return word
        except:
            getpass.getpass('[提示]请输入数字！')


""" 
    @name: statusCode
    @args: None
    @return: str
    @data: 2018-04-20 PM
"""
def statusCode():
    for i in range(3):
        if coupon.passcode == isBlank('领取码'):
            return '200： 领取码验证通过'
        else:
            print('202：输入错误')
    return '201：验证失败，退出程序'



# 主函数入口
if __name__ == '__main__':

    coupon = ElectronicCoupon()

    coupon.ecprice = isBlank('抵卷面值')
    coupon.validity = isBlank('有效期')
    coupon.ecid = time.strftime('%Y%m%d%H%M%S', time.localtime())
    coupon.passcode = random.randint(100000, 999999)
    print('领取码为：', coupon.passcode)

    print(statusCode())
