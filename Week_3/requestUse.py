# -*- Coding:utf-8 -*-
"""
    requestUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    resquest模块的应用
    @author: Manchester
    @data: 2018-04-29
"""


import requests

url = 'http://www.douban.com'
url = 'http://book.douban.com/subject_search'
url = 'http://httpbin.org/get'
url = 'https://httpbin.org/post'

headers ={
        'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
        'Host':'httpbin.org'
}

# response = requests.get(url, data={'search_text':'三体', 'cat':1001})
response = requests.post(url, headers=headers, json={'search_text':'三体', 'cat':1001})
print(response.status_code)
print(response.text)

