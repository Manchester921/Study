# -*- Coding:utf-8 -*-
"""
    fileUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见文件操作
    @author: Manchester
    @data: 2018-04-24
"""

import pickle
import json
import csv
import xlwt
import xlrd
import os


def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf8') as fp:
            return fp.read()
    except UnicodeDecodeError:
        with open(filePath, 'rb') as fp:
            return fp.read()

def writeFile(filePath, fileData):
    try:
        with open(filePath, 'w', encoding='utf8') as fp:
            return fp.write(fileData)
    except TypeError:
        with open(filePath, 'wb') as fp:
            return fp.write(fileData)


def writeKpl(filPath, fileData):
    with open(filPath, 'w') as fp:
        pickle.dump(fileData, fp)

# 重新读取再转化为 bytes 写入
def addKpl(filPath, fileData):          
    content = ''
    with open(filePath, 'rb') as fp:
        content = pickle.load(fp)
    content += fileData                  # 更新数据
    with open(filPath, 'w') as fp:
        pickle.dump(content, fp)        
# 直接写入
def addKpl2(filPath, fileData):           
    with open(filPath, 'ab') as fp:
        pickle.dump(fileData, fp)        # 将fileData 转化为 bytes 写入

def readKpl(filPath):
    with open(filePath, 'rb') as fp:
        while True:
            try:
                content = pickle.load(fp)
                print(content)
            except EOFError:
                break



def writeJson(filePath, fileData):
    pass
def readJson(filePath):
    pass

def writeCsv(filePath, fileData):
    pass
def readCsv(filePath):
    pass

def writeXls(filePath, fileData):
    pass
def readXls(filePath):
    pass


if __name__ == '__main__':

    data = "'name'：'Manchetser', 'age'： 22,'a':123"

    filePath = R'.\files'
    kplPath = os.path.join(filePath, 'fileUse.kpl')
    jsonPath = os.path.join(filePath, 'fileUse.json')
    csvPath = os.path.join(filePath, 'fileUse.csv')
    xlsPath = os.path.join(filePath, 'fileUse.xls')

    addKpl(kplPath, data)




    with open(R'.\files\t.kpl', 'rb') as fp:
        #data1 = pickle.load(fp)
        #print(data1)
        #print(fp.read())

        print('~'*50)
        while True:
            try:
                content = pickle.load(fp)
                print(content)
            except EOFError:
                break

        # content = pickle.load(fp)
        #print(type(data1))
        
    #pickle.dump(data, R'.\Python\Study\Week_3\ads.txt')


    pass
