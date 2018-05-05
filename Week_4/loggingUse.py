# -*- Coding:utf-8 -*-
"""
    loggingUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    logging应用
    @author: Manchester
    @data: 2018-04-29
"""

import logging
import os
import time


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s-')
logDir = R'.\files\logging'
if not os.path.exists(logDir):
    os.mkdir(logDir)
logName = time.strftime('%Y%m%d_%H%M%S', time.localtime()) + '.log'
logPath = logDir + os.sep + logName

fileHandler = logging.FileHandler(logPath)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

consolHandler = logging.StreamHandler()
consolHandler.setLevel(logging.INFO)
consolHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(consolHandler)

print(logPath)
# logging.basicConfig(level = logging.INFO, format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s-')


logger.fatal('')
logger.critical('')
logger.error('')
logger.warning('')
logger.info('')
logger.debug('')

