# -*- Coding:utf-8 -*-
"""
    fileUes2.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见文件操作
    @author: Manchester
    @data: 2018-04-24
"""

import pickle
import os
import json
import time

filePath = R'.\files\data11212.json'

if not os.path.exists(filePath):
    os.mkdir(filePath)

