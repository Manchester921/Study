# -*- Coding:utf-8 -*-
"""
    fileUes2.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见文件操作
    @author: Manchester
    @data: 2018-04-24
"""

import pickle
import os
import json


class Post():
    def __init__(self, pid, title, author, publish, content):
        self.__id = pid
        self.__title = title
        self.__author = author
        self.__publish = publish
        self.__content = content

    def __str__(self):
        return 'id:%s\ttitle:%s\nauthor:%s\tpublish:%s\ncontent:%s\n' % \
                (self.__id, self.__title, self.__author, self.__publish, self.__content)
  


class PostTools():

    def addPost(self, postData):
        with open(filePath, 'w', encoding='utf8') as fp:
            json.dump(postData, fp, ensure_ascii=False)
            print('OOP方法：json文件存储成功~')

    def showPost(self):
        with open(filePath, 'r', encoding='utf8') as fp:
            data = json.load(fp)
            print(data)


def toJson(data):
    with open(filePath, 'w', encoding='utf8') as fp:
        json.dump(data, fp, ensure_ascii=False)
        print('json文件存储成功~')


if __name__ == '__main__':

    filePath = R'.\files\data.json'

    data =[]
    i = 0
    postTool = PostTools()

    while 1:
        i += 1
        print('id =', i)
        title = input('请输入标题:>')
        author = input('请输入作者:>')
        publish = input('请输入时间:>')
        content = input('请输入内容:>')
        post = Post(i, title, author, publish, content)
        content = 'id:%s,\ttitle:%s,\nauthor:%s,\tpublish:%s,\ncontent:%s,\n' % \
                (i, title, author, publish, content)
        data.append(content)
        if input('是否继续输入(y/n):>') != 'y':
            break
    
 
    postTool.addPost(data)
    postTool.showPost()




    #toJson(data)
