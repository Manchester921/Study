#-*- Coding:utf-8-*-
"""
    Work_1_2_1.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    终端接受一个随意输入的十进制数据，输出 二进制、八进制和十六进制
    @author: Manchester
    @data: 2018-04-09 PM
"""

num = int(input('请输入想要转换的数字：'))
print('二进制：%s' % bin(num))
print('八进制：%s' % oct(num))
print('十六进制：%s' % hex(num))

print('二进制转十进制：%s' % int(bin(num),2))
print('二进制转十进制：%s' % int(oct(num),8))
print('二进制转十进制：%s' % int(hex(num),16))





