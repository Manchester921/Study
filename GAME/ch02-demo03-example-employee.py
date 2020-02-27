#-*- coding:utf-8 -*-
'''
    ch01-demo03-example-employee.py
    ------------------------
    pickle模块 序列化读取对象

    @Copyright: Chinasoft International·ETC
    @author: Alvin
    @date: 2018-04-24
'''

# 导入模块
import pickle
import os

# 员工类
class Employee():

    # 构造方法
    def __init__(self, empno, ename):
        self.__empno = empno # 员工编号
        self.__ename = ename # 员工姓名
        pass
    
    # 对象输出
    def __str__(self):
        print('empno: {0}'.format(self.__empno))
        print('ename: {0}'.format(self.__ename))
        return ''   
    
# 员工操作类
class EmployeeDao():

    # 构造方法
    def __init__(self):
        pass
    
    # 添加员工的实例方法
    def addEmployee(self, employee, filePath):
        # 使用with语句完成二进制文件写入
        with open(filePath, 'wb') as fp:
            # 使用dump()序列化并写入文件
            pickle.dump(employee, fp)
            print('提示: 员工添加成功.')
            pass

    # 读取员工数据并显示
    def findAllEmployee(self, filePath):
        # 使用with语句完成二进制文件读取
        with open(filePath, 'rb') as fp:
            # 使用load()读取数据文件并反序列化成对象
            data = pickle.load(fp)
            # 返回结果
            print(data)
            pass

# 脚本入口
if __name__ == '__main__':
    # 设置数据文件的绝对路径地址
    filePath = os.path.join(os.getcwd())

    print('#' * 30)
    print('添加员工信息')
    print('#' * 30)
    # 接收用户输入
    empno = input('empno: ')
    ename = input('ename: ')
    # 创建Employee对象并为属性初始化
    emp = Employee(empno, ename)
    # 创建EmployeeDao操作对象
    empDao = EmployeeDao()
    # 调用empDao对象中的addEmployee()实现对对象持久化存储
    empDao.addEmployee(emp, filePath + os.sep + 'employee.info')
    # 调用empDao对象时中的selectAllEmployee()实现获取对象
    empDao.findAllEmployee(filePath + os.sep + 'employee.info')

    # 导入BytesIO
    from io import BytesIO
    # 创建内存字节存储空间
    f = BytesIO()
    # 将employee对象写入
    f.write(pickle.dumps(emp))
    # # 获取序列化后的员工字节数据
    e = f.getvalue() 
    print(e)
    # 得到反序列化后的员工对象数据
    e = pickle.loads(e)
    print(e)
    
    pass