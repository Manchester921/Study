# -*- Coding:utf-8 -*-
"""
    osUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    os模块的应用
    @author: Manchester
    @data: 2018-04-23 
"""


import threading     # 类方法
import time
import random






count = 0




class Prducer(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.__threadName = threadName
    
    def run(self):
        global count
        while 1:
            if condition.acquire():
                if count >= 10:
                    print('共享区已满，生产者Producter线程进入阻塞状态...')
                    condition.wait()
                else:
                    count += 1
                    print('%s---%s 生产了1件商品并放入缓冲区，当前缓冲区的总数为%s'%\
                         (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.__threadName, count))
                    condition.notify()
                condition.release()
                time.sleep(random.randint(0, 2))

class Customer(threading.Thread):
    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.__threadName = threadName
    
    def run(self):
        global count
        while 1:
            if condition.acquire():
                if count <= 0:
                    print('共享区已空，消费者Customer线程进入阻塞状态...')
                    condition.wait()
                else:
                    count -= 1
                    print('%s---%s 从缓冲区消费了1件商品，当前缓冲区的总数为%s'%\
                         (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), self.__threadName, count))
                    condition.notify()
                condition.release()
                time.sleep(random.randint(0,3))


if __name__ == '__main__':
    condition = threading.Condition()
    threadLock = threading.Lock()
    threads = []

    for i in range(5):
        prducter = Prducer('[生产者-%s]'%(i+1))
        prducter.start()

    for i in range(5):
        customer = Customer('[消费者-%s]'%(i+1))
        customer.start()



    pass

