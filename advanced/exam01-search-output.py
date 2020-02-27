# -*- Coding:utf-8 -*-
"""
    exam01-search-output.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    指定文件夹遍历
    @author: Manchester
    @data: 2018-05-15
"""

import os 

def search(filePath):
    files = os.listdir(filePath)
    print(filePath)
    for fi in files:
        fiPath = os.path.join(filePath, fi)
        with open(R'.\file.txt', 'a',encoding='utf-8' )as fp:
            fp.write(fiPath+'\n')
        print(fiPath)
        if os.path.isdir(fiPath):
            search(fiPath)


search(input('请输入指定路径:>'))


