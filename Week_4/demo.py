
import re
import requests
import urllib.request




a = int(input('sss'))





# class Spider():
#     def __init__(self, search):
#         self.search = search
#         pass


# url = 'https://s.taobao.com/search?q=life&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180505&ie=utf8'
# url = 'https://search.jd.com/Search?enc=utf-8&keyword=三体'
# url = 'https://s.taobao.com/search?q=life'
# url = 'https://search.jd.com/Search?keyword=life'



# url = 'http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10005-1#comfort'
# headers ={'User-Agent':'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)'}

# regExp = re.compile(r'[\s\n]{2,}')
# regItems = re.compile(r'<ul class="clearfix">(.*?)</ul>')
# regItem = re.compile(r'<div class="p-detail">(.*?)</div>')
# regTitle = re.compile(r'class="p-name">(.*?)</a>')
# regAuthor = re.compile(r'<dd>.*?<a.*?>(.*?)</a>')
# regPrice = re.compile(r'<dd><em.*?>(.*?)</em>')


# response = requests.get(url, headers=headers)
# # print(response.status_code)
# # print(response.apparent_encoding)
# # response.encoding = response.apparent_encoding
# response.encoding = 'GB2312'
# content = response.text
# # print(content)


# blockCode = regExp.sub('', content)
# # print(blockCode)
# lstItems = regItems.findall(blockCode)[0]
# # print(lstItems)
# lstItem = regItem.findall(lstItems)
# for i in lstItem:
#     lstTitle = regTitle.findall(i)[0].replace('\u3000', ' ')
#     lstAuthor = regAuthor.findall(i)[0]
#     lstPublish = regAuthor.findall(i)[1]
#     lstPrice = regPrice.findall(i)
#     print('#'*50)
#     print(lstTitle)
#     print(lstAuthor)
#     print(lstPublish)
#     # print(lstPrice)









# print('~'*50)
# response = urllib.request.urlopen(url)

# print('服务器返回的状态码：%s'% response.getcode())
# print('服务器反馈的信息：%s'% response.info())
# content = response.read().decode('gbk')
# # print(content)




#     # data = [{'cpage':i} for i in range(1,25)]

#     # for i in range(24):
#     #     response = requests.get(url, headers=headers, data=data[i])
#     #     # print(response.status_code)
#     #     content = response.text
#     #     lstNews = regNews.findall(content)
#     #     # print(lstNews)
#     #     for news in lstNews:
#     #         lstPublish = regPublish.findall(news)
#     #         lstTitle = regTitle.findall(news)
#     #         lstgAbstract = regAbstract.findall(news)
#     #         print(lstPublish[0] + '\n' + lstTitle[0] + '\n' + lstgAbstract[0].replace('\r\n\t', '') + '\n' + '~'*50)

#     # pass