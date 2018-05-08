# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
import json
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
        


    def process_item(self, item, spider):
        print('>> writ to json...')
        now = time.strftime('%Y%m%d', time.localtime())
        jsonFileName = 'doubanMovie_' +now + '.json'
        try:
            with open(self.folderName + os.sep + jsonFileName, 'a') as jsonFile:
                data = json.dumps(dict(item), ensure_ascii=False) + '\n'
                jsonFile.write(data)
        except IOError as err:
            self.logger.error('IOError')
            raise('json file error:%s' %(str(err)) )
        finally:
            jsonFile.close()
        
        return item
