#-*- Coding:utf-8 -*-
"""
    excelUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    种数据文件格式互相转换的功能脚
    @author: Manchester
    @data: 2018-04-25
"""

import xlwt
import os

excelPath = R'.\files\test.xls'
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('测试单页1')

headers = ['标题1','标题2','标题3','标题4','标题5']

for colIndex in range(len(headers)):
    sheet.write(0, colIndex,headers[colIndex])

for rowIndex in range(1, 50):
    for colIndex in range(len(headers)):
        sheet.write(rowIndex, colIndex, (rowIndex*colIndex))

workbook.save(excelPath)

