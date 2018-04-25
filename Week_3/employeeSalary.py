#-*- Coding:utf-8 -*-
"""
    employeeSalary.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    员工薪资计算   类的继承
    @author: Manchester
    @data: 2018-04-19 
"""

import pickle
class Employee():

    def __init__(self, eid, ename, esalary):
        self.__eid = eid
        self.__ename = ename
        self.__esalary = esalary

    def __str__(self):
        print('编号:>' + self.__eid)        
        print('姓名:>' + self.__ename)
        print('薪水:>' + self.__esalary)
        return ''

class EmaployeeTool():

    def addEmployee(self, filePath, empInfo):
        with open(filePath, 'wb') as fp:
            employee = Employee(empInfo)
            pickle.dump(employee, fp)

    pass

if __name__ == '__main__':

    filePath = R'.\Python\Study\Week_3\employee.kpl'
    