#-*- coding:utf-8 -*-
"""
    baidu_image_crawl.py
    ===============================
    百度关键字搜索图片采集应用示例(体验课-学生版)

    @copyright: Chiansoft International.edu
    @author: Yan He（CTO办公室）
    @date: 2018-01-13 15:34
    @version: v1.5
"""
# 导入相关程序模块
import requests
import os
import re
import itertools
import urllib
import sys

"""
    ====================================
    百度请求地址解密对照表
    ====================================
"""
# 百度请求地址解码对照表
# url地址加密的两种常见方式：（1）单个字符转多字符  （2）单字符对位替换
# url请求抓包地址中的单多字符转单字符解密对照表（字典数据类型）
str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}
# url请求抓包地址中的单字符对位替换解密对照表（字典类型）
char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

# ASCII码转换对照表
# ord()函数的作用是将字符转换成对应的ASCII码
# 使用字典推导式将单个字符对位转换后，再转成ACSII码对照表（字典类型）
char_table = {ord(key): ord(value) for key, value in char_table.items()}


"""
    ====================================
    基础功能函数
    ====================================
"""
# 功能描述：根据url地址解码表解析百度url请求访问地址（生成解密之后的请求地址）
# 参数：字符串类型 url
# 返回值：字符串类型（解密后的url请求地址）
# 作者：------
# 开发时间：2017-12-28 11:37
# 最后修改时间：2017-12-31 13:15
def decode(url):
    # 使用for循环遍历字符对照表所有选项
    for key, value in str_table.items():
        # 使用replace()函数进行对位转换
        url = url.replace(key, value)
    # 使用 translate()函数完成url地址解密转换并返回
    return url.translate(char_table)

# 功能描述：完成百度图片的自动下拉加载搜索更多
# 参数：字符串类型 word（搜索关键字，多个用空格分隔）
# 返回值：元组类型（图片搜索url下拉加载更多的请求连接地址）
# 作者：------
# 开发时间：2017-12-30 10:10
def buildUrls(word):
    # 使用quote()函数实现对特殊字符的处理
    word = urllib.parse.quote(word)
    # 设置搜索请求url地址
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=60"
    # 使用元组推导式完成对所有分页页面的地址创建
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=60))
    # 返回请求地址数据集
    return urls

# 定义一个解析图片对象地址的正则表达式对象，后续用于解析获取图片的真实地址
re_url = re.compile(r'"objURL":"(.*?)"')

# 功能描述：解析请求结果响应页面的HTML源代码，使用re_url规则解析得到所有搜索图片对象的url链接地址
# 参数：字符串类型 html（搜索结果页面源代码）
# 返回值：列表类型（存放所有符合搜索条件的图片url链接地址）
# 作者：------
# 开发时间：2017-12-30 14:40
def resolveImgUrl(html):
    # 使用列表推导式获取并解析页面所有的所搜图片url连接地址，并用decode()函数进行解密
    imgUrls = [decode(x) for x in re_url.findall(html)]
    # 返回所有图片的地址
    return imgUrls

# 功能描述：下载指定url地址请求的图片
# 参数1：字符串 imgUrl（图片url地址）
# 参数2：字符串 dirpath (图片下载存放路径)
# 参数3：字符串 imgName (图片自定义名称)
# 参数4：字符串 imgType (图片后缀名)
# 返回值：布尔类型
# 作者：------
# 开发时间：2018-01-06 12:10
def downImgs(imgUrl, dirpath, imgName, imgType):
    # 设置图片文件存储路径
    filename = os.path.join(dirpath, imgName)
    try:
        # 使用get()函数发送访问请求并设置超时时限
        res = requests.get(imgUrl, timeout=15)
        # 判断服务器请求返回码，若为 '4xx'开头均为拒绝访问报错代码
        if str(res.status_code)[0] == '4':
            # 输出错误码及图片链接地址信息
            print(str(res.status_code), ":", imgUrl)
            # 返回False终止当前操作
            return False
    except Exception as e:
        print('抛出异常:', imgUrl)
        print(e)
        return False
    # 使用文件二进制写入方式创建本地图片文件的引用链接
    with open(filename + '.' + imgType, 'wb') as f:
        # 向指定的路径写入请求返回的图片数据
        f.write(res.content)
    # 返回True，表示下载成功
    return True

# 功能描述：创建图片下载本地文件夹
# 参数：字符串 dirName（存储图片文件夹名称）
# 返回值：字符串（图片存储地址）
# 作者：------
# 开发时间：2017-12-31 17:10
def mkDir(dirName):
    # 创建图片文件夹相对路径地址
    dirpath = os.path.join(sys.path[0], dirName)
    # 判断地址是否存在?
    if not os.path.exists(dirpath):
        # 创建文件夹地址
        os.mkdir(dirpath)
    # 返回文件夹地址路径
    return dirpath

# main脚本程序入口
if __name__ == '__main__':

    print("="*50)
    print("欢迎使用百度图片下载爬虫")
    print("@copyright: Chiansoft International.edu 2017-2018")
    print("="*50)

    # 完成任务1：设置数据采集参数
    # 1-1:保存路径
    choosePath = int(input("\nStep1:请输入您想要保存路径的方式\n\n\
    1、默认路径 path = images/\n\n\
    2、相对路径 Path = Path_input/path/\n\n\
    3、绝对路径 Path = D:\images/\n\n\
    \n(请选择(1~3):>"))
    if choosePath == 3:
        dirPath = input('请输入您要保存的位置：')
    elif choosePath == 2:
        path = input('请输入您要保存的位置：')
        dirPath = mkDir(path)
    elif choosePath == 1:
        path = 'images'
        dirPath = mkDir(path)
    else:
        print('请输入正确的参数!')
    print('~'*50)

    # 1-2: 搜索关键字

    word = input('Step2:请输入您想要搜索关键字:>\n\n')
    print('~'*50)

    # 1-3：保存图片的格式

    chooeImgType = int(input('Step3:请输入您想要保存的图片格式:>\n\n\
 1.jpg\n 2.png\n 3.gif\n\n请选择(请选择(1~3):>'))
    if chooeImgType == 3:
        imgType = 'gif'
    elif chooeImgType == 2:
        imgType = 'png'
    elif chooeImgType == 1:
        imgType = 'jpg'
    else:
        print('请输入正确的参数!')
    print('~'*50)

    # 1-4:图片进行命名附加信息

    strTag = input('Step3:请输入您想要下载图片的名字:>\n\
    最后格式为 number+' '+name.%s\n\n' % imgType)
    print('~'*50)

    # 1-5:下载图片数量
    numImg = int(input('Step3:请输入您想要下载图片数量:>\n'))

    # 完成任务2：调用前置函数完成业务组合

    urls = buildUrls(word)
    index = 0 
    print('~'*50)
    
    for url in urls:
        print('正在发送请求...')
        html = requests.get(url, timeout = 2).content.decode('utf-8')
        print('requests')
        imgUrls = resolveImgUrl(html)
        
    
    # 循环遍历每一个图片访问地址
#    for url in imgUrls:
        if downImgs(url, dirPath, str(index+1)+strTag,imgType):
            index += 1
            print('已经下载了{0}'.format(index))

        if index == numImg:
            break


        

