#-*- Coding:utf-8 -*-
"""
    FilesCategory.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    函数编程磁盘分类文件统计
    @author: Manchester
    @data: 2018-04-20 PM
"""

import os

""" 
    @name: recursionSearch
    @args: str 文件路径, tuple 不定数目参数的后缀名
    @return: bool
    @data: 2018-04-20 PM
"""
def recursionSearch(filePath, *suffixs):
    '''函数编程磁盘分类'''
    global statistic
    files = os.listdir(filePath)

    for fi in files:
        fiPath = os.path.join(filePath, fi)
        print(fiPath)
        if os.path.isdir(fiPath):
            recursionSearch(fiPath, *suffixs)
        else:
            for suffix in suffixs:
                if fi.endswith(suffix):
                    statistic[suffix] += 1

#主函数入口
if __name__ == '__main__':

    os.system('cls')
    statistic = {}
    suffixs = input('请输入想要检索的文件名后缀(用逗号分开):>').split(',')
    for suffix in suffixs:
        statistic[suffix] = 0
    path = input('请输入想要检索的文件夹路径:>')
    recursionSearch(path, *suffixs)
    for suffix in statistic:
        print('文件名后缀为 %s 有%s个' % (suffix, statistic[suffix]))





