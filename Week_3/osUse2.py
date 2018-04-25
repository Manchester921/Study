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

class LogInfo():

    def __init__(self):
        self.__logTime = None
        self.__filePath = None
        self.__fileName = None
        self.__dirName = None
        
    @property
    def logTime(self):
        return self.__logTime
    @logTime.getter
    def logTime(self):
        return self.__logTime
    @logTime.setter
    def logTime(self, value):
        self.__logTime = value

    @property
    def filePath(self):
        return self.__filePath
    @filePath.getter
    def filePath(self):
        return self.__filePath
    @filePath.setter
    def filePath(self, value):
        self.__filePath = value

    @property        
    def fileName(self):
        return self.__fileName
    @fileName.getter
    def fileName(self):
        return self.__fileName
    @fileName.setter
    def fileName(self, value):
        self.__fileName = value

    @property        
    def dirName(self):
        return self.__dirName
    @dirName.getter
    def dirName(self):
        return self.__dirName
    @dirName.setter
    def dirName(self, value):
        self.__dirName = value


class FileTools():
    def fileWalk(self, filePaths):
        for root,dirs,files in os.walk(filePaths):
            fileInfo = LogInfo()
            fileInfo.logTime = time.strftime('%Y%m%d %H%M%S', time.localtime())
            fileInfo.filePath = root
            fileInfo.fileName = files
            fileInfo.dirName = dirs
            with open('.\\%s.log' % fileInfo.logTime, 'a', encoding='utf8') as fp:
                fp.write('%s\n%s\n当前路径下的文件夹有:>%s\n当前路径下的文件有:>%s\n' % (fileInfo.logTime,fileInfo.filePath, fileInfo.fileName, fileInfo.dirName))



if __name__ == '__main__':
    filePath = input('请输入需要查找的文件:>')
    try:
        files = FileTools()
        files.fileWalk(filePath)
        print('文件写入成功！')
    except FileNotFoundError:
        print('没有找到该文件\a')