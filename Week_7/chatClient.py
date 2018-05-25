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
import _thread
import threading
import os


"""
    @name: listenThread
    @args: conn
    @return: none98+    
    @data: 2018-05-21
"""
def listenThread(conn):
    while 1:
        replay = conn.recv(4096).decode('utf-8')
        print(replay)


def recvThread(conn):
    name = input('请输入昵称:>')
    conn.send(name.encode())
    while 1:
        massage = input()
        if massage == 'quit':
            break
        conn.send(massage.encode())
        # print('[OK] 客户端成功像服务器发送了数据')

        




host = 'localhost'
port = 6869
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('[OK] 成功创建sockte对象')
    remoteIP = socket.gethostbyname(host)
    print('[OK] %s IP:%s'%(host, remoteIP))
    s.connect((remoteIP, port))
    print('[OK] 客户端成功连接远端服务器%s:%s'%(remoteIP, port))
    # replay = s.recv(4096).decode()
    # print(replay)

    th1 = threading.Thread(target=listenThread, args=(s,))  
    th2 = threading.Thread(target=recvThread, args=(s,))

    threads = [th1, th2]   
    for t in threads :  
        t.setDaemon(True)  # 设置线程为守候线程在后台运行
        t.start()  # 启动线程
    t.join()

except socket.error as msg:
    print('[Error:%s] socket创建失败 >> %s'%(str(msg), msg)) 
    sys.exit()
except socket.gaierror as msg:
    print('[Error:%s] 获取服务器IP地址失败 >> %s' %(str(msg[0]), msg[1]))
finally:
    s.close()
    print('[OK] 关闭socket套接字对象')
    os.system('pause')


