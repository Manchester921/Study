#-*- Coding:utf-8-*-
"""
    bubbleSort.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    冒泡排序
    @author: Manchester
    @data: 2018-04-13 PM
"""

import random 

sortList = [random.randint(1, 500) for i in range(50)]
print(sortList)
for i in range(len(sortList),0,-1):
    for j in range(i-1):
        if (sortList[j] > sortList[j + 1]):      
            pass
            sortList[j], sortList[j+1] = sortList[j+1], sortList[j]

print(sortList)

    

