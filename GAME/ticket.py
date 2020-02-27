# -*- Coding:utf-8 -*-
"""
    ticket.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    火车售票系统
    @author: Manchester
    @data: 2018-04-27
"""
import threading
import time
import random
import json
ticketUse = 100
ticket = 100

class TicketWindow(threading.Thread):
    def __init__(self, windowID):
        threading.Thread.__init__(self)
        self.__windowID = windowID
        self.__seatID = None
    def run(self):
        global  sat, satUse, ticket, ticketUse
        while 1:
            if ticket <= 0:
                break
            if ticketUse <= 0:
                time.sleep(1)
                continue
            self.__customerID = random.randint(10000,99999)
            print('[售票窗口%s]  顾客%s进入窗口>>>顾客正在操作中...'% (self.__windowID, self.__customerID))
            time.sleep(random.random()*3)  
            while 1:
                try:
                    self.__seatID = random.sample([i for i in satUse if satUse[i] == 1],1)[0] 
                except ValueError:
                    print('[售票窗口%s]  座位已售空'%self.__windowID)
                    return 
                if condition.acquire():
                    if satUse[self.__seatID] == 1:
                        ticketUse -= 1
                        satUse[self.__seatID] = 0
                        print('[售票窗口%s]  为顾客%s预留%s号座位  >>>  目前还剩%s张未被预定的票'\
                                %(self.__windowID, self.__customerID, self.__seatID, ticketUse))
                    condition.release()
                    break
            while 1:
                print('[售票窗口%s]  等待顾客%s支付  >>>顾客正在操作中...'%(self.__windowID, self.__customerID))
                time.sleep(random.random()*5)
                if random.random() <= 0.7:
                    # print('正在支付中...')
                    if condition.acquire():
                        if sat[self.__seatID] == 1:
                            ticket -= 1
                            sat[self.__seatID] = 0
                            print('[售票窗口%s]  顾客%s支付成功%s号座位已经售出  目前还剩%s张票  >>>%s'\
                                    %(self.__windowID, self.__customerID, self.__seatID, ticket,\
                                     time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
                            addInfo = {self.__seatID : self.__customerID }
                            satInfo = {}
                            with open(filePath, 'r', encoding='utf8') as fp:
                                satInfo = json.load(fp)
                            satInfo.update(addInfo)
                            with open(filePath, 'w', encoding='utf8') as fp:
                                json.dump(satInfo, fp, ensure_ascii=False)
                        condition.release()
                        break
                else:
                    print('[售票窗口%s]  顾客%s未支付!  >>>交易失败...'%(self.__windowID, self.__customerID))
                    ticketUse += 1
                    satUse[self.__seatID] += 1
                    break
                    
# 主程序入口
if __name__ == '__main__':
    condition = threading.Condition()
    threads = []
    filePath = R'.\files\ticketInfo.json'
    with open(filePath, 'w', encoding='utf8') as fp: 
        json.dump({}, fp, ensure_ascii=False)
    satUse = dict(zip(list(range(100)),[1]*100))
    sat = dict(zip(list(range(100)),[1]*100))
    for i in range(20):
        ticketWindow = TicketWindow('%s'%(i))
        ticketWindow.start()
        threads.append(ticketWindow)
    for i in threads:
        i.join()
    print('>>>售票结束...')
    print(ticket, ticketUse)
    print('~'*50)
    print(sat)
    print(satUse)
    print('~'*50)
    
    with open(filePath, 'r', encoding='utf8') as fp:
        print(json.load(fp))




