# -*- Coding:utf-8 -*-
"""
    urlDownload.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    多线程下载任务
    @author: Manchester
    @data: 2018-04-27
"""

import threading     
import urllib.request
import os
import pickle
import socket
from urllib import request
import sys
import time

class DownloadThread(threading.Thread):
    def __init__(self, url, savePath, fileName, threadNum):
        threading.Thread.__init__(self)
        self.url = url
        self.savePath = savePath
        self.fileName = fileName
        self.threadNum = threadNum
        self.contentLength = None
        self.per = 0
    
    def run(self):
        # os.system('cls')
        # fileType = self.__fileName.split('.')[-1]
        local_fileName, headers = urllib.request.urlretrieve(self.url, self.savePath, self.schedule)
        # self.contentLength = int(headers['Content-Length'])
        # print(local_fileName)
        # print(headers)
        # print(contentLength)

    def schedule(self, block, blocksize, contentLength):
        self.per = 100*block*blocksize/contentLength
        self.contentLength = contentLength
        if self.per > 100:
                self.per = 100
      
 
if __name__ == '__main__':
    url = ['https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi',
           'https://www.python.org/ftp/python/3.6.5/python-3.6.5.exe']
    
    condition = threading.Condition()
    threads = []
    fileName = [i.split('/')[-1] for i in url]
    for i in range(2):
        downloadThread = DownloadThread(url[i], R'.\files\%s'% fileName[i], fileName[i], i)
        downloadThread.start()
        threads.append(downloadThread)
    while 1:
        os.system('cls')
        print('~'*70)
        for i in threads:
            print('文件名称:> %10s\t\t'% i.fileName, end='')
        print()
        for i in threads:
            print('文件大小:> %10s 字节\t\t'% i.contentLength, end='')   
        print()
        for i in threads:
            print('Download progress:> %d%%\t\t\t'%  i.per, end='')
        print()
        print('~'*70)
        time.sleep(0.2)
        if sum([i.per for i in threads]) == len(threads)*100:
            break
        
    print('>>>下载结束...')



    # downloadThread.join()    



