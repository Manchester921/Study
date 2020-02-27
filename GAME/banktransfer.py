#-*- coding:utf-8 -*-
"""
    banktransfer.py
    ~~~~~~~~~~~~~~~~~
    银行支票阿拉伯数字转汉字的功能
"""
#准备转换列表
a = ['零','壹','貳','叁','肆','伍','陆','柒','捌','玖']
b = ['圆','拾','佰','仟','萬']

#step1: 编写代码来接收输入的5位以内的数字：
money = int(input('请输入所需转换的5位以内金额：'))
m1=money
#print(type(money))

#step2: 计算输入数字的位数
count = 0
while(money > 0):
    money = int(money/10)
    count += 1
print(count)

#step3：拆分每一位上的数字 进行对应输出
for i in str(m1):
    print(a[int(i)]+b[count-1],end="")
    count -= 1


