# -*- Coding:utf-8 -*-
"""
    mergeSort.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    冒泡排序 归并排序 阶乘
    @author: Manchester
    @data: 2018-05-03
"""

import random 
import time

# 冒泡排序
def bubbleSort(list1):
    for i in range(len(list1),0,-1):
        for j in range(i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1
    


# 归并排序
def mergeSort(list1):
    if len(list1) == 1:
        return list1
    if len(list1) == 2:
        return list1 if list1[0]<list1[1] else list1[::-1]
    if len(list1) >= 3:                                     # 分裂子列
        middle = len(list1)//2
        listLeft = mergeSort(list1[0:middle])   
        listRight = mergeSort(list1[middle:])

    leftIter, rightIter = iter(listLeft), iter(listRight)   # 生成迭代器
    a, b = next(leftIter), next(rightIter)
    listSort = []
    while 1:                                                # 依次对比排序 。。。
        if a <= b:
            listSort.append(a)
            try:
                a = next(leftIter)
            except StopIteration:
                listSort.append(b)
                while 1:
                    try:
                        listSort.append(next(rightIter))
                    except StopIteration:
                        return listSort
        else:
            listSort.append(b)
            try:
                b = next(rightIter)
            except StopIteration:
                listSort.append(a)
                while 1:
                    try:
                        listSort.append(next(leftIter))    
                    except StopIteration:
                        return listSort



# 归并排列  优雅版

def merge(a, b):
    c = []
    h = j = 0
    while j < len(a) and h < len(b):     # ！！！！！！！！
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    return c


def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])
    return merge(left, right)





if __name__ == '__main__':

    # print(list1)

    # list2 = list1
    # print('计时开始 >> 冒泡排序ing')
    # startTime = time.time()
    # res1 = bubbleSort(list2)
    # endTime = time.time()
    # print ('计时结束 >> 冒泡排序耗时：%f s' % (endTime - startTime))
    # # print(res1)

    list1 = [random.randint(1,99999999) for i in range(1000000)]       # 生成随机序列

    list2 = list1
    print('计时开始 >> 归并排序ing')
    startTime = time.time()
    res2 = mergeSort(list2)
    endTime = time.time()
    print ('计时结束 >> 耗时：%f s' % (endTime - startTime))
    # print(res2)

    list2 = list1
    print('计时开始 >> 归并排序(优雅版)ing')
    startTime = time.time()
    res3 = merge_sort(list2)
    endTime = time.time()
    print ('计时结束 >> 耗时：%f s' % (endTime - startTime))
    # print(res3)

    
    list4 = list1
    print('计时开始 >> 系统排序ing')
    startTime = time.time()
    list4.sort()
    endTime = time.time()
    print ('计时结束 >> 耗时：%f s' % (endTime - startTime))
    # print(list4)

    print(res2 == res3 == list4)

    # 阶乘
    fac = lambda n: 1 if n==1 else n*fac(n-1)
    # print(fac(9))

