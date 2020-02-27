# -*- Coding:utf-8 -*-
"""
    IOUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    文件IO操作
    @author: Manchester
    @data: 2018-04-23 
"""

def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf8') as fp:
            return fp.read()
    except UnicodeDecodeError:
        with open(filePath, 'rb') as fp:
            return fp.read()

def writeFile(filePath, content):
    try:
        with open(filePath, 'w', encoding='utf8') as fp:
            return fp.write(content)
    except TypeError:
        with open(filePath, 'wb') as fp:
            return fp.write(content)

if __name__ == '__main__':

    content = readFile(R'D:\workspace\Python\Study\Python\test\PIC\1.png')
    writeFile(R'D:\workspace\Python\Study\Python\test\PIC\3.png', content)

    content = 'print("Hello World!")\ninput("Manchester")'
    writeFile(R'lalala~.py', content)
