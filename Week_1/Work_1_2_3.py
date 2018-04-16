#-*- Coding:utf-8-*-
"""
    Work_1_2_3.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    字符串函数的应用
        将网址进行加密操作，将网址中的?、=、&字符转码ASCII后，在以十六进制
        输出。网址样本为：http://www.mywebsit.com/?query=python&count=20
        编写成加密后并输出url：http://www.mywebsit.com/0x3fquery0x3dpyth
        on0x26count0x3d20再编写代码进行解密还原原始的url地址并输出。
    @author: Manchester
    @data: 2018-04-09 PM
"""

url = 'http://www.mywebsit.com/?query=python&count=20'
print('原地址为：\t\t',url)

changeSign = ['?', '=', '&']
for i in changeSign:
    url = url.replace(i,str(hex(ord(i))))
print('转换后的地址为：\t',url)

while(url.find('0x') != -1):
    before = url[url.find('0x'):url.find('0x')+4]
    back = chr(int(before,16))
    url = url.replace(before,back)
print('转换回来的地址为：\t',url)

