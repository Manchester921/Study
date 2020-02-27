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
import _thread

host = ''
port = 6869


"""
    @name: clientThread
    @args: conn
    @return: none
    @data: 2018-05-21
"""
def clientThread(conn):
    sendData = '[OK] 您已成功连接到服务器'+'\n\r'
    conn.sendall(bytes(sendData, encoding='gb2312'))
    while 1:
        data = conn.recv(1024)
        data = 'Server>>' + str(data, encoding='gb2312') + '\n\r'
        if data:
            conn.send(bytes(data, encoding='gb2312'))



try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[OK] 成功创建sockte对象')
    s.bind((host, port))
    s.listen(5)
    while 1:
        print('[OK] 服务器启动监听')
        conn, addr = s.accept()
        print('[OK] 客户端%s成功接入服务器，访问端口号%s'%(addr[0], addr[1]))
        # print(conn)
        _thread.start_new_thread(clientThread, (conn,))
        print('服务器成功创建一个线程处理')


except socket.error as msg:
    print('[Error:%s] socket创建失败 >> %s'%(str(msg), msg)) 
    sys.exit()
except socket.gaierror as msg:
    print('[Error:%s] 获取服务器IP地址失败 >> %s' %(str(msg[0]), msg[1]))
    sys.exit()
finally:
    conn.close()
    print('[OK] 关闭连接对象')
    s.close()
    print('[OK] 关闭socket套接字对象')



