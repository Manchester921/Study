#-*- Coding:utf-8 -*-
"""
    classMathod.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    计算器类
    @author: Manchester
    @data: 2018-04-18 PM
"""


class ClassName():

    classVariable = 0

    def __init(self):
        self.instanceVariable = 0

    @classmethod
    def classMethod(cls, arg1):
        print('classMathode类方法。。。')
        print('>>',arg1)

        cls.classVariable += 1
        # cls.instanceVariable -= 1      # 不能运算  只能赋值  ？？？？
        cls.instanceVariable = 'eeeee'
        

        print('classVariable:', cls.classVariable)

    def method(self, arg):
        self.classMethod(arg)

if __name__ == '__main__':
    ClassName.classMethod('hello!') 

    instanceObj = ClassName()
    instanceObj.classMethod('lalala~')

    
    instanceObj.method('Manchester')

    print(instanceObj.classVariable)


