#-*- Coding:utf-8 -*-
"""
    excelUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    种数据文件格式互相转换的功能脚
    @author: Manchester
    @data: 2018-04-25
"""

import xlwt
import xlrd
import os
import json
import csv


data =  [{'姓名':'Manchester', '性别':'男', '年龄':22},
         {'姓名':'lalala~', '性别':'女', '年龄':18},
         {'姓名':'Lucifer', '性别':'男', '年龄':19}, 
         {'姓名':'Eclipse', '性别':'男', '年龄':21}]

keys = [key for key in data[0]]
print(keys)

dataList = [[item[key] for key in keys] for item in data]
print(dataList)

excelPath = R'.\files\test.xls'
workbook = xlwt.Workbook(encoding='utf-8')
sheet = workbook.add_sheet('测试单页1')

headers = keys

for colIndex in range(len(headers)):
    sheet.write(0, colIndex,headers[colIndex])

for rowIndex in range(1, len(dataList)+1):
    for colIndex in range(len(headers)):
        sheet.write(rowIndex, colIndex, (dataList[rowIndex-1][colIndex]))

workbook.save(excelPath)

print('~'*50)


workbook = xlrd.open_workbook(excelPath)

sheets = workbook.sheet_names()

worksheet = workbook.sheet_by_name(sheets[0])
for rowIndex in range(worksheet.nrows):
    rowData = worksheet.row(rowIndex)
    for colIndex in range(worksheet.ncols):
        print(worksheet.cell_value(rowIndex, colIndex), '\t\t',end='')
    print('')



print('~'*50)

def jsonToexcel():
    with open(jsonPath, 'r', encoding='utf8') as fp:
        global content
        content = json.load(fp)
        print(content)
        print('json文件读取成功~')
        
    print(content)

    keys = [key for key in content[0]]
    dataList = [[item[key] for key in keys] for item in content]

    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('测试单页1')

    headers = [key for key in content[0]]

    for colIndex in range(len(headers)):
        sheet.write(0, colIndex,headers[colIndex])

    for rowIndex in range(1, len(dataList)+1):
        for colIndex in range(len(headers)):
            sheet.write(rowIndex, colIndex, (dataList[rowIndex-1][colIndex]))

    workbook.save(excelPath)
    pass

jsonPath = R'.\files\data.json'
jsonToexcel()

content



print('~'*50)


def excelTojson():
    pass

    
workbook = xlrd.open_workbook(excelPath)

sheets = workbook.sheet_names()

worksheet = workbook.sheet_by_name(sheets[0])


data = []
print(worksheet.row(1).value())
for rowIndex in range(1,worksheet.nrows):
    rowData = worksheet.row(rowIndex)
    data.append(dict(zip(worksheet.row(1), rowData)))
print(data)
    # for colIndex in range(worksheet.ncols):
    #     print(worksheet.cell_value(rowIndex, colIndex), '\t\t',end='')
    #     worksheet.cell_value(rowIndex, colIndex)
    # print('')

data = []
#worksheet.row(1, worksheet.nrows)

data = [dict(zip(worksheet.row(0) ,rowData)) for rowData in [worksheet.row(rowIndex) for rowIndex in range(1,worksheet.nrows)]]

print(data)

