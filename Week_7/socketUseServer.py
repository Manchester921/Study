# -*- Coding:utf-8 -*-
"""
    exam01-search-output.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    socket应用
    @author: Manchester
    @data: 2018-05-21
"""

import socket
import sys

host = ''
port = 6869

massage = 'GET / HTTP/1.1\r\n\r\n'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[OK] 成功创建sockte对象')
    s.bind((host, port))
    s.listen(5)
    while 1:
        print('[OK] 服务器启动监听')
        conn, addr = s.accept()
        print('[OK] 客户端%s成功接入服务器，访问端口号%s'%(addr[0], addr[1]))
        print(conn)
        sendData = '[OK] 您已成功连接到服务器'
        conn.sendall(bytes(sendData, encoding='gb2312'))


except socket.error as msg:
    print('[Error:%s] socket创建失败 >> %s'%(str(msg), msg)) 
    sys.exit()
except socket.gaierror as msg:
    print('[Error:%s] 获取服务器IP地址失败 >> %s' %(str(msg[0]), msg[1]))
    sys.exit()
finally:
    conn.close()
    print('[OK] 关闭conn连接对象')
    s.close()
    print('[OK] 关闭socket套接字对象')



