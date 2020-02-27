#-*- Coding:utf-8 -*-
"""
    run.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    运行doubanMovie爬虫
    @author: Manchester
    @data: 2018-04-25
"""


from scrapy.cmdline import execute

execute(['scrapy', 'crawl', 'movieInfo'])

