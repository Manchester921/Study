# -*- Coding:utf-8 -*-
"""
    loggingUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    logging应用
    @author: Manchester
    @data: 2018-04-29
"""


import pymysql

def dbExcutrSQL(sql):
    dbServerIP = 'localhost'
    user = 'root'
    password = ''
    # dbName = 'rentdatabase'
    dbName = 'doubanmovie'

    try:
        connection = pymysql.connect(host=dbServerIP, port=3306, user=user,\
                                    password=password, db=dbName, charset='utf8')
        print('>> 数据库连接成功.')
        print('>> sql: %s'%sql)
        cursor = connection.cursor()
        addectRows = cursor.execute(sql)
        connection.commit()
        print('>> 事务提交.')
        return addectRows
    except pymysql.err.OperationalError:
        print('>> 数据库IP地址或账号密码错误，请核实...')
    except pymysql.err.InternalError:
        print('>> 数据库没有找到，请核实...')
    except:
        connection.rollback()
        print('>> 操作失败 事物回滚')
    finally:
        connection.close()
        print('>> 数据库连接已关闭.')


item={'rank':['1'], 'title':['肖生克的救赎'],\
     'link':['www'], 'rating':['9.8'],\
     'participants':['1021021'], 'quote':['自由'], }

print('>> writ to mySQL...')
info = []
info.append(int(item['rank'][0]) )
info.append(item['title'][0]) 
info.append(item['link'][0]) 
info.append(float(item['rating'][0]))
info.append(int(item['participants'][0].replace('人评论', '')))
info.append(item['quote'][0]) 
sql = R"insert into movieInfo value(%d, '%s', '%s', %f, %d, '%s') "\
                %(info[0], info[1], info[2], info[3], info[4], info[5])

dbExcutrSQL(sql)














def dbQuerySQL(sql):
    dbServerIP = 'localhost'
    user = 'root'
    password = ''
    dbName = 'rentdatabase'
    try:
        connection = pymysql.connect(host=dbServerIP, port=3306, user=user,\
                                    password=password, db=dbName, charset='utf8')
        print('>> 数据库连接成功.')
        print('>> sql: %s'%sql)
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print('>> 查询成功.')
        return result
    except pymysql.err.OperationalError:
        print('>> 数据库IP地址或账号密码错误，请核实...')
    except pymysql.err.InternalError:
        print('>> 数据库没有找到，请核实...')
    except:
        connection.rollback()
        print('>> 操作失败')
    finally:
        connection.close()
        print('>> 数据库连接已关闭.')

sql1 = R"insert into lessor value(null, '%s', '%s', '%s', '%s') "\
        %('usertest01', '123456', '测试用户1', '2018-05-07')
sql2 = R"select * from lessor"
sql3 = R"select * from rentinghouse where rhprice<10000"
sql4 = R"update rentinghouse set rhprice=rhprice*1.1 "

print(dbExcutrSQL(sql1))
result = dbQuerySQL(sql2)
for item in result:
    print(item)
result = dbQuerySQL(sql3)
for item in result:
    print(item)
print(dbExcutrSQL(sql4))
