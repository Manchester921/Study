# -*- Coding:utf-8 -*-
"""
    osUes.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    os模块的应用
    @author: Manchester
    @data: 2018-04-23 
"""

import threading     # 类方法
import _thread       # 函数方法
import time

class MyThread(threading.Thread):
    def __init__(self, threadName, delay):
        threading.Thread.__init__(self)
        self.__threadName = threadName
        self.__delay = delay

    def run(self):
        print('[启动]>>>%s启动运行...'% self.__threadName)


        workThread(self.__threadName+'启动程序', 2)
        threadLock.acquire()
        workThread(self.__threadName, self.__delay)
        threadLock.release()

        print('[停止]>>>%s停止运行...'% self.__threadName)
        pass




def workThread(name, delay):
    for i in range(delay):
        print('  |- %s正在执行中...%s %s' %\
             (name, i+1, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        time.sleep(1)




if __name__ == '__main__':


    
    threadLock = threading.Lock()
    threads = []

    print('>>>主线程MainThread正在执行...')

    # 函数形式 主线程结束 子线程未结束 会报错
    # _thread.start_new_thread(workThread, ('Thread-1', 5,)) 
    # _thread.start_new_thread(workThread, ('Thread-2', 3,))

    thread01 = MyThread('MyThread-1', 5)
    thread02 = MyThread('MyThread-2', 3)
    thread01.start()
    thread02.start()

    for i in range(2):
        time.sleep(1)
        print('>>>主线程MainThread正在执行中...', i+1)
    print('>>>主线程运行完毕 正在等待子线程结束...')
    
    threads.append(thread01)
    threads.append(thread02)
    for t in threads:
        t.join()

    print('>>>主线程MainThread已经停止...')