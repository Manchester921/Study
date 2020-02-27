# -*- Coding:utf-8-*-
"""
    Work_1_2_3.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    字符串函数的应用   二 八 十六 进制转换  
    @author: Manchester
    @data: 2018-04-09 PM
"""


num = int(input('请输入想要转换的数字：'))
print('二进制：%s' % bin(num))
print('八进制：%s' % oct(num))
print('十六进制：%s' % hex(num))

print('二进制转十进制：%s' % int(bin(num),2))
print('二进制转十进制：%s' % int(oct(num),8))
print('二进制转十进制：%s' % int(hex(num),16))





url = 'http://www.mywebsit.com/?query=python&count=20'
print('原地址为：\t\t', url)

changeSign = ['?', '=', '&']
for i in changeSign:
    url = url.replace(i, str(hex(ord(i))))
print('转换后的地址为：\t', url)

while(url.find('0x') != -1):
    before = url[url.find('0x'):url.find('0x')+4]
    back = chr(int(before, 16))
    url = url.replace(before, back)
print('转换回来的地址为：\t', url)




posts = [{'id': 1, 'title': '测试标题1', 'author': '匿名用户1',
          'publish': '2018-01-01', 'content': '这里是帖子的测试内容1……',
          'replay': [{'publish': '2018-01-06', 'content': '这里是回复内容1……'},
                     {'publish': '2018-01-05', 'content': '这里是回复内容2……'}]},
         {'id': 2, 'title': '测试标题2', 'author': '匿名用户3',
          'publish': '2018-02-11', 'content': '这里是帖子的测试内容2……',
          'replay': [{'publish': '2018-02-15', 'content': '这里是回复内容3……'},
                     {'publish': '2018-01-12', 'content': '这里是回复内容4……'}]}, ]

print('论坛帖子\n' + '='*50)
for postId in posts:
    print('postId:', postId['id'])
    print('title:', postId['title'])
    print('author:', postId['author'])
    print('publish:', postId['publish'])
    print('-'*50)
    print(postId['content'], '\n')
    for replay in postId['replay']:
        print('回复<%s>:%s' % (replay['publish'], replay['content']))
    print('\n')
