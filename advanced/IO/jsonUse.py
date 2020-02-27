# -*- Coding:utf-8 -*-
"""
    IOUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    文件IO操作
    @author: Manchester
    @data: 2018-04-23 
"""

import json
import csv

if __name__ == '__main__':

    data = {'name':'Manchester', 'age':22, 'gander':'男'}

    res1 = json.dumps(data, ensure_ascii=False)
    print(res1)
    obj = json.loads(res1)
    print(obj)
    print(type(obj))
    

    with open(R'.\Python\Study\Week_3\employee.json', 'w', encoding='utf8') as fp:
        json.dump(data, fp, ensure_ascii=False)
        print('处理完毕')

    with open(R'.\Python\Study\Week_3\employee.json', 'r', encoding='utf8') as fp:
        res2 = json.load(fp)
        print(res2)



    columns = ['姓名', '性别', '年龄']
    csvdata = [('Manchester', '男', 21),
                ('lalala~', '女', 20)]
#
    with open(R'.\Python\Study\Week_3\test.csv', 'w', encoding='gb18030', newline='') as fp:

        writer = csv.writer(fp)
        writer.writerow(columns)
        writer.writerows(csvdata)

        print('处理完毕')



    pass


