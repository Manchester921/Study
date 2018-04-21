# -*- Coding:utf-8 -*-
"""
    gameLife.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    游戏人生
    @author: Manchester
    @data: 2018-04-16 
"""

import getpass
import os
import random
import sys
import time


class GameLife():

    def __init__(self, name, gender):
        self.name = name
        self.gander = gender
        self.fighting = 1000

    def menu(self):
        print('\n\n'+'='*15, '人在江湖 游戏人生', '='*15,
              '\n玩家姓名：%s\t玩家性别：%s\t玩家战斗力%s\t'
              % (self.name, self.gander, self.fighting))
        print('#'*50, '\n\t1.草场战斗\n\t2.多人战斗\n\t3.闭关修炼\n\t4.随机参加\n'+'#'*50)
        return input('请输入要参加游戏:>')

    def __status(self, fightingName, change):
        self.fighting += change
        print('\n\t参加%s,%s%s战斗力' %
              (fightingName, ['增长', '消耗'][change < 0], change))
        for i in range(25):
            print(' ', end='>', flush=True)
            time.sleep(0.02 * random.random() * i)
        if self.fighting <= 0:
            print('\n玩家阵亡，游戏结束！')
            getpass.getpass('[%s]隐退江湖...' % self.name)
            sys.exit(0)
        else:
            print('\n%s完成！' % fightingName)
            getpass.getpass('\t[%s]所剩战斗力：%s' % (self.name, self.fighting))
            return

    def fightingGame(self, num):
        if num == '1':
            self.__status('草场战斗', -200)
        elif num == '2':
            self.__status('多人战斗', -500)
        elif num == '3':
            self.__status('闭关修炼', 300)
        elif num == '4':
            self.fightingGame(str(random.randint(1, 3)))
        else:
            getpass.getpass('<错误>请输入1~3的数字')


if __name__ == '__main__':
    os.system('cls')
    name = input('请输入玩家姓名:>')
    gender = input('请输入玩家性别:>')
    getpass.getpass('[%s]进入江湖！又是一场腥风血雨~' % name)

    player = GameLife(name, gender)
    while True:
        os.system('cls')
        num = player.menu()
        player.fightingGame(num)
