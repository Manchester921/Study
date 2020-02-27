# -*- Coding:utf-8 -*-
"""
    exam01-search-output.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    socket应用
    @author: Manchester
    @data: 2018-05-15
"""

import socket
import sys

host = 'www.baisu.com'
host = 'www.douban.com'
port = 80
massage = 'GET / HTTP/1.1\r\n\r\n'
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[OK] 成功创建sockte对象')
    remoteIP = socket.gethostbyname(host)
    print('[OK] %s IP:%s'%(host, remoteIP))
    s.connect((remoteIP, port))
    print('[OK] 客户端成功连接远端服务器%s:%s'%(remoteIP, port))
    s.send(massage.encode())
    print('[OK] 客户端成功像服务器发送了数据')
    replay = s.recv(4096)
    print(replay.decode())

except socket.error as msg:
    print('[Error:%s] socket创建失败 >> %s'%(str(msg), msg)) 
    sys.exit()
except socket.gaierror as msg:
    print('[Error:%s] 获取服务器IP地址失败 >> %s' %(str(msg[0]), msg[1]))
finally:
    s.close()
    print('[OK] 关闭socket套接字对象')



