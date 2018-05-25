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
import time
import os


def timeNow():return time.strftime('<%Y-%m-%d %H:%M:%S>', time.localtime())

"""
    @name: clientThread
    @args: conn
    @return: none
    @data: 2018-05-21
"""
def clientThread(conn):
    try:
        # print(conn)
        clientName = str(conn.recv(4096).decode('utf-8'))
        clients.update({clientName:conn})
        sendData = '[server] %s进入聊天室' %clientName
        print(sendData)
        broadcastDate(conn, sendData)
        while 1:
            data = str(conn.recv(4096).decode('utf-8'))
            massage = '\r\f\r[%s] %s' %(clientName, data)
            print(massage)
            broadcastDate(conn, massage)
    except ConnectionResetError:
        try:
            del clients[clientName] 
            massage = '[server] %s已退出聊天室' %clientName
            print(massage)
            broadcastDate(conn, massage)
        except UnboundLocalError:
            print('[server] 未命名用户退出聊天室')



"""
    @name: broadcastDate
    @args: conn, str
    @return: none
    @data: 2018-05-22
"""
def broadcastDate(sendConn, massage):
    for client in clients:
        connClient = clients[client]
        if connClient != sendConn:
            connClient.send(bytes(massage, encoding='utf-8'))


if __name__ == '__main__':
    host = ''
    port = 6869
    clients = {}

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('[server] 成功创建sockte对象')
        s.bind((host, port))
        s.listen(5)
        print('[server] 服务器启动监听ing\n'+'#'*50+'\n')
        while 1:
            conn, addr = s.accept()
            _thread.start_new_thread(clientThread, (conn,))
            print('[server] 服务器成功创建一个线程处理')
            print('[server] 客户端%s:%s成功接入服务器，等待用户输入昵称ing'%(addr[0], addr[1]))
            
    except socket.error as msg:
        print('[Error:%s] socket创建失败 >> %s'%(str(msg), msg)) 
        sys.exit()
    except socket.gaierror as msg:
        print('[Error:%s] 获取服务器IP地址失败 >> %s' %(str(msg[0]), msg[1]))
        sys.exit()
    except :
        print('[Error]')
    finally:
        conn.close()
        print('[server] 关闭连接对象')
        s.close()
        print('[server] 关闭socket套接字对象')
        os.system('pause')

