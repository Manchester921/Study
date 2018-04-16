#-*- Coding:utf-8-*-
"""
    emailSend.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    使用SMTP模块发送邮件
    @author: Manchester
    @data: 2018-04-10 PM
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header

fromAddr = 'testMail921@163.com'
toAddr = ''
authorWord = 'testMail921'

message = MIMEText('我正在学习Python，使用STMP完成简单的邮件发送~~', 'plain', 'utf-8')
message['From'] = Header('Manchester')
message['To'] = Header('My Love')
message['Subject'] = Header('Python3测试邮件', 'utf-8')

try:
    server = smtplib.SMTP('smtp.163.com',25)
    server.login(fromAddr, authorWord)
    server.sendmail(fromAddr, [toAddr], message.as_string())
    print('邮件发送成功!')
    server.quit()
except:
    print('[错误]请输入正确邮箱')


