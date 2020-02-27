# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import time
import json
import pymysql
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

        pass

    def dbExcutrSQL(self, sql):
        dbServerIP = 'localhost'
        user = 'root'
        password = ''
        dbName = 'doubanmovie'
        try:
            connection = pymysql.connect(host=dbServerIP, port=3306, user=user,\
                                        password=password, db=dbName, charset='utf8')
            self.logger.info('数据库连接成功 执行：%s'% sql)
            cursor = connection.cursor()
            addectRows = cursor.execute(sql)
            connection.commit()
            self.logger.info('事务提交')
            return addectRows
        except pymysql.err.OperationalError:
            self.logger.error('数据库IP地址或账号密码错误')
            pass
        except pymysql.err.InternalError:
            self.logger.error('数据库没有找到')
            pass
        except:
            connection.rollback()
            self.logger.error('操作失败 事物回滚')
            pass
        finally:
            connection.close()
            self.logger.info('数据库连接已关闭')
            pass


    def process_item(self, item, spider):
        print('>> writ to mySQL...')
        info = []
        info.append(int(item['rank'][0]) )
        info.append(item['title'][0]) 
        info.append(item['link'][0]) 
        info.append(float(item['rating'][0]))
        info.append(int(item['participants'][0].replace('人评价', '')))
        info.append(item['quote'][0]) 
        sql = R"insert into movieInfo value(%d, '%s', '%s', %f, %d, '%s') "\
                        %(info[0], info[1], info[2], info[3], info[4], info[5])

        self.dbExcutrSQL(sql)

        return item
