#-*- coding:utf-8 -*-
"""
    github_repositor.py
    ~~~~~~~~~~~~~~~~~~~~~~~
    实现github代码仓库中Python代码可视化
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
import requests
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
result = requests.get(url)
print('数据访问状态链：',result.status_code)

json_data = result.json()

repositories = json_data['items']
github_repositor_name = [repository['name'] for repository in repositories]
github_repositor_count = [repository['stargazers_count'] for repository in repositories]

print('\nname数据集：' , github_repositor_name)
print('\nstargazers_count数据集：' , github_repositor_count)

text = ','.join(github_repositor_name)
print('字符串处理程序：',text)

wordcloud = WordCloud().generate(text)

plt.figure()
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()

