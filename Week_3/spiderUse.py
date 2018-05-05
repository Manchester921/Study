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


url = 'http://www.chinasofti.com/newsroom/news.jsp'
headers ={
        'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
        'Host':'httpbin.org'
}

regNews = re.compile(r'<div.*?class="newsNav">(.*?)</div>',re.S  )
regPublish = re.compile(r'<i.*?>(.*?)</i>')
regTitle = re.compile(r'<a.*?>(.*?)</a>')
regAbstract = re.compile(r'<p.*?>(.*?)</p>', re.S|re.M)

data = [{'cpage':i} for i in range(1,25)]

for i in range(24):
    response = requests.get(url, headers=headers, data=data[i])
    # print(response.status_code)
    content = response.text
    lstNews = regNews.findall(content)
    # print(lstNews)
    for news in lstNews:
        lstPublish = regPublish.findall(news)
        lstTitle = regTitle.findall(news)
        lstgAbstract = regAbstract.findall(news)
        print(lstPublish[0] + '\n' + lstTitle[0] + '\n' + lstgAbstract[0].replace('\r\n\t', '') + '\n' + '~'*50)




