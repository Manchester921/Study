# -*- Coding:utf-8 -*-
"""
    reUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    re模块的应用
    @author: Manchester
    @data: 2018-04-28
"""



import requests
import re
import os
import json
import threading
import time
import random


url = 'https://book.douban.com/top250?start='
headers ={'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}




regContent = re.compile(r'<tr class="item">(.*?)</tr>',re.S  )
regExp = re.compile(r'[\s\n]{2,}')
regTitle = re.compile(r'<div class="pl2">.*?title="(.*?)">', re.S|re.M)
regLink = re.compile(r'<a href="(.*?)"')
regRating = re.compile(r'<span class="rating_nums">(.*?)</span>')
regreviews = re.compile(r'<span class="pl">\((.*?)\人\评\价\)</span>')
regBookInfo = re.compile(r'<p class="pl">(.*?)</p>')




url = 'https://book.douban.com/subject/1770782/'
headers ={'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}
regIntro = re.compile(r'<div class="intro"><p>(.*?)</p></div>', re.S)
regComContent = re.compile(r'<div property="v:description".*?data-author="(.*?)" data-url=.*?>(.*?)</div></div>' , re.S)



response = requests.get(url, headers=headers)
content = response.text
blockCode = regExp.sub('', content)
print(blockCode)
lstContent = regIntro.findall(blockCode)
lstComment = regComContent.findall(blockCode)


lstBookInfo = lstContent[-2].replace('</p><p>', '\n')
lisAuthorInfo = lstContent[-1]
print(lstBookInfo)
print(lisAuthorInfo)
print(lstContent)
print(lstComment)




# data = [url + str(i) for i in range(250) if i%25 == 0]
# # print(data)

# rank = 0
# dictBook = []

# for page in data:
#     response = requests.get(page, headers=headers)
#     content = response.text
#     lstContent = regContent.findall(content)
#     # print('#'*50)
#     # print(page)
#     # print(response.status_code)
#     # print(lstContent)
#     for book in lstContent:
#         blockCode = regExp.sub('', book)
#         lstTitle = regTitle.findall(blockCode)[0]
#         lstLink = regLink.findall(blockCode)[0]
#         lstRating = regRating.findall(blockCode)[0]
#         lstreviews = regreviews.findall(blockCode)[0]
#         lstBookInfo = regBookInfo.findall(blockCode)[0].split(' / ')
#         # print(lstTitle)
#         lstAuthor = lstBookInfo[0]
#         if len(lstBookInfo) == 5:
#             lstAuthor += ' %s译'% lstBookInfo[1]
#         rank += 1
#         bookInfo = {'排名':rank, '书名':lstTitle, '链接':lstLink, '得分':lstRating,\
#                          '评价人数':lstreviews,'作者':lstAuthor, '出版社':lstBookInfo[-3],\
#                          '出版日期':lstBookInfo[-2], '售价':lstBookInfo[-1] }
#         dictBook.append(bookInfo)
#         bookResponse = requests.get(lstLink, headers=headers)
#         bookContent = bookResponse.text
#         # print(bookContent)
#         # print('~'*50)
#         # print(blockCode)
#         # print(lstTitle)
#         # print(lstLink)
#         # print(lstRating)
#         print(bookInfo)

# print(dictBook)


# fileDir = R'.\files'
# if not os.path.exists(fileDir): os.mkdir(fileDir)
# filePath = fileDir + os.sep + 'dictBook.json '   
# with open(filePath, 'w', encoding='utf8') as fp:
#     json.dump(dictBook, fp, ensure_ascii=False)



