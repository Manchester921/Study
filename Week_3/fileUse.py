# -*- Coding:utf-8 -*-
"""
    fileUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    常见文件操作
    @author: Manchester
    @data: 2018-04-24
"""

import pickle
import os









if __name__ == '__main__':

    data = "'name'：'Manchetser', 'age'： 22,'a':123"

    with open(R'.\Python\Study\Week_3\t.kpl', 'ab') as fp:
        pickle.dump(data, fp)
        print(type(pickle.dump(data, fp)))
        print('data数据对象序列化写入成功！')

    with open(R'.\Python\Study\Week_3\t.kpl', 'rb') as fp:
        #data1 = pickle.load(fp)
        #print(data1)
        #print(fp.read())

        print('~'*50)
        while True:
            try:
                content = pickle.load(fp)
                print(content)
            except EOFError:
                break

        # content = pickle.load(fp)
        #print(type(data1))
        
    #pickle.dump(data, R'.\Python\Study\Week_3\ads.txt')


    pass
