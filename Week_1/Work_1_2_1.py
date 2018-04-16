#-*- Coding:utf-8-*-
"""
    Work_1_2_1.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    字符串函数的应用
        控制台接受输入的邮箱地址 jack.zhou @163.com 。根据以往的规范，pop3
        和smtp接发服务器的地址为 pop3.163.com 和 smtp.163.com。编写程序自
        动完成发送和接受服务器地址的输出。
    @author: Manchester
    @data: 2018-04-09 PM
"""

mail = input('请输入转换的邮箱地址：')
#mail = 'jack.zhou@163.com'
mailSplit = mail.split('@')
mailSplit[0] = 'pop3'
print('.'.join(mailSplit))
mailSplit[0] = 'smtp'
print('.'.join(mailSplit))
