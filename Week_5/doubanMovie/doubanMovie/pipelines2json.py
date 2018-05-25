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

content = []

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
        self.jsonFilePath = self.folderName + os.sep + 'doubanMovie_' +now + '.json'



  


    def process_item(self, item, spider):
        print('>> writ to json...')
        # items = {k:item[k][0] for k in item}
        # content.append(json.dumps(items, ensure_ascii=False))

        # try:
        #     with open(jsonFilePath, 'w') as jsonFile:
        #         data = json.dumps(content, ensure_ascii=False)
        #         jsonFile.write(data)
        # except IOError as err:
        #     self.logger.error('IOError')
        #     raise('json file error:%s' %(str(err)) )
        # finally:
        #     jsonFile.close()

        with open(self.jsonFilePath, 'a')as jsonFile:
            print(dict(item))
            line = json.dumps(dict(item),ensure_ascii=False ) + "\n"
            jsonFile.write(line)        




        return item
