#-*- Coding:utf-8-*-
"""
    goodsInfo.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    排序。。。。
    @author: Manchester
    @data: 2018-04-10 PM
"""

nums = input('请输入需要排列的数字(使用空格间隔)').split()

intNum = []
for i in list(range(len(nums))):
    intNum.append(int(nums[i]))

intNum.sort()
print('数字排序后的结果为：', intNum)



