# -*- Coding:utf-8 -*-
"""
    ticket.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    火车售票系统
    @author: Manchester
    @data: 2018-04-27
"""



import urllib.request
import os
import pickle
import socket

from urllib import request




if __name__ == '__main__':

    url = 'http://www.baidu.com'
    url = 'http://book.douban.com/subject_search'
    url = 'http://www.douban.com'
    url = 'https://www.python.org/static/img/python-logo.png'
    url = 'http://httpbin.org/post'


    headers = {
        'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
        'Host':'httpbin.org'
    }

    req = request.Request(url=url, headers=headers, method='POST')
    response = request.urlopen(req)
    print(response.getcode())
    fileName = url.split('/')[-1]
    print(fileName)
    data = urllib.request.urlopen(url).read()
    with open(R'.\files\%s'% fileName, 'wb') as fp:
        fp.write(data)    



    dicPrarms = {'search_text':'三体', 'cat':1001}
    data = pickle.dumps(dicPrarms)

    # try:
    response = urllib.request.urlopen(url)
    # except socket.timeout:
    #     print('连接请求超时...')


    print('服务器返回的状态码：%s'% response.getcode())
    print('服务器反馈的信息：%s'% response.info())
    print('~'*50)
    content = response.read().decode('utf-8')
    print(content)
    with open(R'.\files\urlUse.html', 'w', encoding='utf-8') as fp:
        fp.write(content)

