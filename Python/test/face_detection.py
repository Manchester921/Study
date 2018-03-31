#-*- coding:utf-8 -*-
"""
    face_detction.py
    ~~~~~~~~~~~~~~~~~
    百度 AIP  人脸特征识别 
"""

#步骤1：导入百度AIP的AirFace
from aip import AipFace

#步骤2：导入APPID数据
APP_ID = '11221477'
AIP_KEY = 'p7n5TX9Mu0vIzSZie8u09K2w'
SECRET_KEY = 'y1XN6NlBlxfokFUeOmfmCzVBzRlewsOm'
#步骤3：创建百度智能云对象client
client = AipFace(APP_ID,AIP_KEY,SECRET_KEY)

#步骤4:创建图取图片函数
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#步骤5：调用函数读取图片
face_image = get_file_content("Python/test/PIC/1.png")



#步骤6：设置option选项
option = {}
option["face_fields"] = "age,gender,beauty"

#步骤7：使用client对象 完成人脸识别分析
data = client.detect(face_image,option)

print(data)






