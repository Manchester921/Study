#-*- Coding:utf-8 -*-
"""
    decoration.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    面向对象    
    @author: Manchester
    @data: 2018-04-17 PM
"""

class Product():

    def __init__(self):
        self.__pname = None
        self.__pid = None
    
    def __str__(self):
        print('[Pid:%s, Pname:%s]' % (self.__pid, self.__pname))
        return ''
    

    @property
    def pid(self):
        return self.__pid
    
    @pid.getter
    def pid(self):
        return self.__pid

    @pid.setter
    def pid(self, value):
        self.__pid = value
        pass


    @property
    def pname(self):
        return self.__pname
    
    @pname.getter
    def pname(self):
        return self.__pname

    @pname.setter
    def pname(self, value):
        self.__pname = value
        pass


if __name__ == '__main__':
    product = Product()

    product.pid = 1
    product.pid = '测试商品'


    print(product.pid)
    print(product.pname)

    print(product)

    print('#'*50, '\n')

    listProduct = []

    def generatorProduct():

        for i in range(10):
            product = Product()
            product.pid = i + 1
            product.pname = '测试商品'

            yield product


    for product in generatorProduct():
        print(product)
        



