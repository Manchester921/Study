#-*- coding=utf-8 -*-
"""
    file_path.py
    ~~~~~~~~~~~~~~~~~~
    文件检索
"""
import(os)
def iter_path(filePath)
    #步骤1：遍历指定位置的文件
    files = os.listdir(filePath)
    #步骤2：for循环遍历数据集合
    for fi in files:
        #拼接组合后的绝对路径
        fi_d = os.path.join(filePath,fi)
        #判断是否为文件夹
        if os.path.isdir(fi_d):
            iter_path(fi_d)
        else:
            print("-->{0}".format(fi_d))

iter_path("d:" + os.sep + "gzj")
