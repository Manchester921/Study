# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
import xlwt
import xlrd
from xlutils.copy import copy
import logging
import time

class DoubanmoviePipeline(object):
    def __init__(self):
        self.folderName = 'output'
        if not os.path.exists(self.folderName):
            os.mkdir(self.folderName)
            
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s-')
        logName = time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.log'
        logPath = self.folderName + os.sep + logName

        fileHandler = logging.FileHandler(logPath)
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)


        now = time.strftime('%Y%m%d', time.localtime())
        excelFileName = 'doubanMovie_' + now + '.xls'
        self.excelPath = self.folderName + os.sep + excelFileName
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet('豆瓣电影数据')
        headers = ['电影排名', '电影名称', '电影链接', '电影评分', '参评人数', '电影摘引']
        # headers = [key for key in item]
        for colIndex in range(len(headers)):
            self.sheet.write(0, colIndex,headers[colIndex])
        self.rowIndex = 1
        self.workbook.save(self.excelPath)


    def process_item(self, item, spider):
        print('>> writ to excel...')

        oldWb = xlrd.open_workbook(self.excelPath, formatting_info=True)
        newWb = copy(oldWb)
        sheet = newWb.get_sheet(0)

        # line = [item['rank'], item['title']]
        line = [item[key] for key in item]
        

        for colIndex in range(len(item)):
            sheet.write(self.rowIndex, colIndex, line[colIndex])
        
        newWb.save(self.excelPath)
        self.rowIndex += 1



        
        return item
