#-*- coding:utf-8 -*-
"""
    decorate.py
    ~~~~~~~~~~~~~~~~~
    统计时间装饰器函数
"""
# 导入time模块
import time
# 自定义一个统计时间的高阶函数
def calcTime(func):
	print ('--> 开始计时.....')
	startTime = time.time() # 使用time()获取时间戳
	func()  # 调用传入的函数
	endTime = time.time()  # 使用time()再获取时间戳
	print ('--> 结束计时.....')
	msecs = (endTime - startTime) * 1000  # 计算两次时间差
	# 输出结果
	print ('--> 性能测试结果：' + func.__name__ + '函数耗时：%f ms' % msecs)


# 自定义一个测试函数，装饰器方式，无需调用
@ calcTime
def func1():
	print ('func1() start...')
	time.sleep(0.6)  # 模拟0.6秒执行
	print ('func1() end...')







#-*- coding:utf-8 -*-
"""
    demo07.py
    ~~~~~~~~~~~~~~~~
    闭包的应用
"""

# case01：闭包基本应用
def foo():
    m = 1
    n = 2
    # 定义一个内部函数（闭包）
    def bar():
        a = 3
        return m + n + a
    # foo()必须有return子句，而且必须返回内部函数对象
    return bar

# 调用
fun = foo() # fun的类型为函数类型<class: function>
print(foo()())
print(type(fun))
print(fun()) # 闭包调用方法，执行foo()->bar()

# case02. 闭包根据不同的配置信息（参数）得到不同的结果
def make_addr(var1):
    def addr(var2):
        return var1 + var2
    return addr

p1 = make_addr(23)
print(p1(100))  # 123

# case03. 装饰器 + 闭包
# HTML：<b><i>hello</i></b>

def makebold(fn): # 自身高阶函数
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn): # 自身高阶函数
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeitalic
@makebold
def hello():
    return "Hello,中软国际"

print(hello())



