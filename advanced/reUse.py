# -*- Coding:utf-8 -*-
"""
    reUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    re模块的应用
    @author: Manchester
    @data: 2018-04-28
"""


import re

print(re.match(r'^\d{3}\-\d{3,8}$', '132-55555'  ))

reg1 = re.compile(r'^\d{3}\-\d{3,8}$')
reg1.match('132-55555')
print(reg1.match('132-553355'))

reg3 = re.compile(r'^(\d{3})(\-)(\d{3,8})$')
m = reg3.match('139-6656998')
print(m)
print(m.group(1))




content = '<div class="a">张三</div><div class="b">李四</div><div class="a">王五</div>'

regName = re.compile(r'<div.*?class="a">(.*?)</div>')
listName = regName.findall(content)
print(listName)




