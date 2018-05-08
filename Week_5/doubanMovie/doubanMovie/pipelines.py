# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os
import logging
import time

class DoubanmoviePipeline(object):
    def __init__(self):
        self.folderName = 'output'
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)
        if not os.path.exists(R'.\output\pic'):
            os.mkdir(R'.\output\pic')

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s-')
        logName = time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.log'
        logPath = self.folderName + os.sep + logName

        consolHandler = logging.StreamHandler()
        consolHandler.setLevel(logging.INFO)
        consolHandler.setFormatter(formatter)
        fileHandler = logging.FileHandler(logPath)
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(formatter)

        self.logger.addHandler(consolHandler)
        self.logger.addHandler(fileHandler)


    def process_item(self, item, spider):
        
        # print('电影排名：%s' %(item['rank'][0]) )
        # print('电影名称：%s' %(item['title'][0]) )
        # print('电影链接：%s' %(item['link'][0]) )
        # print('电影评分：%s' %(item['rating'][0]) )
        # print('参评人数：%s' %(item['participants'][0]) )
        # print('电影摘引：%s' %(item['quote'][0]) )

        imgUrl = item['picSrc'][0]
        picName = item['rank'][0] +'_'+ item['title'][0]
        try:
            r=requests.get(imgUrl, timeout=2)
            path = R'.\output\pic\%s.webp'% (picName)
            with open(path,'wb') as f:  
                f.write(r.content) 
        except requests.exceptions.ConnectTimeout:
            self.logger.error('%s图片下载超时'% picName )
            

        

        self.logger.info('电影排名：%s' %(item['rank'][0]) )
        self.logger.info('电影名称：%s' %(item['title'][0]) )
        self.logger.info('电影链接：%s' %(item['link'][0]) )
        self.logger.info('电影评分：%s' %(item['rating'][0]) )
        self.logger.info('参评人数：%s' %(item['participants'][0]) )
        self.logger.info('电影摘引：%s' %(item['quote'][0]) )





        return item