#-*- Coding:utf-8-*-



# #asda
# print('验')

# def w1(func):
#     def inner():
#         print('验证2')
#         return func()
#     print('验证1')
#     inner()
#     print('验证3')

#     return inner
 
# @w1
# def f1():
#     print('f1')

# f1()

#






# import time
# time.strftime('%Y%m%d%H%M%S',time.localtime())
# timeNow = int(time.time())
# print(timeNow)
# print(time.time())
# print(time.localtime(time.time()))
# print(time.strftime('%Y%m%d%H%M%S',time.localtime()))








# def w1(func):
#     def inner(*args,**kwargs):
#         print('验证1',*args)
#         return func(*args,**kwargs)
#     return inner
 
# def w2(func):
#     def inner(*args,**kwargs):
#         print('验证2',*args)
#         return func(*args,**kwargs)
#     return inner
 
 
# @w1
# @w2
# def f1(arg1,arg2,arg3):
#     print ('f1')


# f1(1, 2, 3)








def decorate(func):
    print('#'*20)
    func()
    print('#'*20)
    pass

@decorate
def aaa():
    print('aaa')

aaa()








