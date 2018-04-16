#-*- Coding:utf-8-*-
"""
    goodsInfo.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    字典列表嵌套数据提取
    @author: Manchester
    @data: 2018-04-12 PM
"""

posts = [{'id':1, 'title':'测试标题1', 'author':'匿名用户1', 
          'publish':'2018-01-01', 'content':'这里是帖子的测试内容1……',
          'replay':[{'publish':'2018-01-06', 'content':'这里是回复内容1……'},
                    {'publish':'2018-01-05', 'content':'这里是回复内容2……'}]}, 
         {'id':2, 'title':'测试标题2', 'author':'匿名用户3', 
          'publish':'2018-02-11','content':'这里是帖子的测试内容2……',
          'replay':[{'publish':'2018-02-15', 'content':'这里是回复内容3……'},
                    {'publish':'2018-01-12', 'content':'这里是回复内容4……'}]},]

print('论坛帖子\n' + '='*50)
for postId in posts:
    print('postId:', postId['id'])
    print('title:', postId['title'])
    print('author:', postId['author'])
    print('publish:', postId['publish'])
    print('-'*50)
    print(postId['content'],'\n')
    for replay in postId['replay']:
        print('回复<%s>:%s' % (replay['publish'], replay['content']))
    print('\n')

