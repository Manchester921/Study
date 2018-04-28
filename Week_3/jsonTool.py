# -*- Coding:utf-8 -*-
"""
    fileUes3.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见文件操作
    @author: Manchester
    @data: 2018-04-24
"""

import pickle
import os
import json

class jsonTools():

    def __init__(self, filePath):
        self.__filePath = filePath
        try:
            with open(self.__filePath, 'r', encoding='utf8') as fp:
                self.__content = json.load(fp)
                print(self.__content)
                input('原始json文件读取成功~')
        except FileNotFoundError:
            self.__content = [] if input('<错误\a>没有找到该json文件,\
                请输入需要创建的json文件类型(list/dict)默认为list:>').lower != 'dict' else {}
            with open(self.__filePath, 'w', encoding='utf8') as fp: 
                json.dump(self.__content, fp, ensure_ascii=False)     
        self.__jsonType = type(self.__content)

    def addJson(self, addData):
        if self.__jsonType != type(addData):
            input('<错误\a>输入数据类型与文件数据类型不匹配！')
            return
        elif self.__jsonType == list:
            self.__content += addData
        elif self.__jsonType == dict:
            self.__content.update(addData)
        with open(self.__filePath, 'w', encoding='utf8') as fp:
            json.dump(self.__content, fp, ensure_ascii=False)
            print('json文件存储成功~')

    def showJson(self):
        with open(self.__filePath, 'r', encoding='utf8') as fp:
            print(json.load(fp))
            input('json文件读取成功~')


class Post():
    def __init__(self, pid, title, author, publish, content):
        self.__id = pid
        self.__title = title
        self.__author = author
        self.__publish = publish
        self.__content = content

    def __str__(self):
        print('id:%stitle:%sauthor:%spublish:%scontent:%s' % \
                (self.__id, self.__title, self.__author, self.__publish, self.__content))
        return ''

if __name__ == '__main__':
    # data1 = {'Manchester':['男', 22],'lalala~':['女', 18],
    #         'Lucifer':['男', 19], 'Eclipse':['男', 21]}
    # data2 = [{'姓名':'Manchester', '性别':'男', '年龄':22},
    #         {'姓名':'lalala~', '性别':'女', '年龄':18},
    #         {'姓名':'Lucifer', '性别':'男', '年龄':19}, 
    #         {'姓名':'Eclipse', '性别':'男', '年龄':21}]
    filePath = R'.\files\data.json'
    jsonTool = jsonTools(filePath)

    os.system('cls')
    data = []
    i = 0
    while 1:
        os.system('cls')
        i += 1
        print('请输入信息：\n帖子id:', i)
        title = input('请输入标题:>')
        author = input('请输入作者:>')
        publish = input('请输入时间:>')
        content = input('请输入内容:>')
        post = Post(i , title, author, publish, content)
        dictcontent = post.__dict__
        data.append(dictcontent)
        if input('是否继续输入(y/n):>').lower() != 'y':
            break

    jsonTool.addJson(data)
    jsonTool.showJson()






