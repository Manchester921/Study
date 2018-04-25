# -*- Coding:utf-8 -*-
"""
    osUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    os模块的应用
    @author: Manchester
    @data: 2018-04-23 
"""

import os
from os.path import join, getsize
import time 

absolutePath = os.path.realpath(__file__)
print(__file__)
print('当前文件绝的对路径地址:>', absolutePath)

absoluteDir = os.path.dirname(absolutePath)
print('当前文件目录的绝对地址:>', absoluteDir)
absolutePath.split('\\')[-1]

fileName = os.path.basename(absolutePath)
print(absolutePath.split('\\')[-1])
print('当前文件的名称:>', fileName)

projectDir = os.getcwd()
print('当前工程的绝对路径地址:>', projectDir)

fileSize = os.path.getsize(absolutePath)
print('当前路径的文件的大小为：%s字节' % fileSize)

createTime = os.path.getctime(absolutePath)
accessTime = os.path.getatime(absolutePath)
modifyTime = os.path.getatime(absolutePath)

toTime = lambda timeStamps : time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(timeStamps)).encode('utf8', 'ignore').decode('GBK', 'ignore')
print(type(toTime(createTime)))
print('当前路径文件的创建的时间戳：%s' % toTime(createTime))
print('当前路径文件的最后访问的时间戳：%s' % toTime(accessTime))
print('当前路径文件的最后修改的时间戳：%s' % toTime(modifyTime))

#help('os')
print('~'*50)

def fileInfo(filePath):
    #os.system('cls')
    absolutePath = os.path.realpath(filePath)
    fileName = os.path.basename(absolutePath)
    if os.path.isdir(filePath):
        size = 0
        for root,dirs,files in os.walk(filePath):
            size +=  sum([getsize(join(root, filename)) for filename in files])
    else:
        size = os.path.getsize(absolutePath)

    createTime = os.path.getctime(absolutePath)
    accessTime = os.path.getatime(absolutePath)
    modifyTime = os.path.getatime(absolutePath)
    toTime = lambda timeStamps : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timeStamps)).encode('GBK', 'ignore').decode('utf8', 'ignore')



    print('文件对象的名称:>', fileName)
    print('文件对象的类型:>', ['文件', '文件夹'][os.path.isdir(filePath)])  
    print('文件对象的地址:>', absolutePath)
    print('文件对象的大小:> %s字节' % size)
    print('文件对象的创建时间:> %s' % toTime(createTime))
    print('文件对象的修改时间:> %s' % toTime(modifyTime))
    print('文件对象的访问时间:> %s' % toTime(accessTime))

if __name__ == '__main__':
    filePath = input('请输入需要查找的文件:>')
    try:
        fileInfo(filePath)
    except FileNotFoundError:
        print('没有找到该文件\a')