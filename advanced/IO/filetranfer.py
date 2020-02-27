#-*- Coding:utf-8 -*-
"""
    filetranfer.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    种数据文件格式互相转换的功能脚
    @author: Manchester
    @data: 2018-04-24
"""

import json
import csv


class FileConverter():
    def jsonTocsv(self, jsonPath, csvPath):
        
        with open(jsonPath, 'r', encoding='utf8') as fp:
            global content
            content = json.load(fp)
            print('json文件读取成功~')
        with open(csvPath, 'w', encoding='gb18030', newline='') as fp:
            writer = csv.writer(fp)
            writer.writerows(content)
            print('csv文件写入成功~')



# with open(jsonPath, 'r') as fp:
#     data = json.load(jsonfile)
#     print('>>json文件读取完毕')


# with open(csvPath, 'w', newline='') as fp:
#     keys = [k for k in data[0]]
#     dictWriter = csv.DictWriter(fp, fieldnames=keys)
#     dictWriter.writeheader()
#     for item in data:
#         dictWriter.writerow(item)




    def csvTojson(self, csvPath, jsonPath):
        contentcsv = []
        with open(csvPath, 'r', encoding='gb18030', newline='') as fp:
            # reader = csv.reader(fp)
            # for line in reader:
            #     contentcsv.append(line)
            reader = csv.DictReader(fp)
            listItem = [dict(item) for item in reader]
            print(listItem)

            print('csv文件读取成功~')
        with open(jsonPath, 'w', encoding='utf8') as fp:
            jsondata = json.dumps(contentcsv, ensure_ascii=False)
            fp.write(jsondata)
            print('json文件写入成功~')


if __name__ == '__main__':
    
    content = {}
    file1 = FileConverter()
    file1.jsonTocsv(R'.\files\data.json', R'.\files\data.csv' )
    file1.csvTojson(R'.\files\test.csv', R'.\files\test.json' )

    data =  [{'姓名':'Manchester', '性别':'男', '年龄':22},
            {'姓名':'lalala~', '性别':'女', '年龄':18},
            {'姓名':'Lucifer', '性别':'男', '年龄':19}, 
            {'姓名':'Eclipse', '性别':'男', '年龄':21}]


