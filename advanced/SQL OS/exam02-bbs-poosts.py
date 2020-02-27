# -*- Coding:utf-8 -*-
"""
    exam02-bbs-poosts.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    数据库操作
    @author: Manchester
    @data: 2018-05-15
"""



import pymysql

""" 
    @name: addPosts
    @args: str
    @return: int
    @data: 2018-04-11 PM
"""
def addPosts(sql):
    """插入数据库内容"""
    dbServerIP = 'localhost'
    user = 'root'
    password = ''
    dbName = 'postdb'

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

""" 
    @name: showPosts
    @args: None
    @return: list/tuple/None
    @data: 2018-04-11 PM
"""
def showPosts():
    """展示数据库内容"""
    dbServerIP = 'localhost'
    user = 'root'
    password = ''
    dbName = 'postdb'
    try:
        connection = pymysql.connect(host=dbServerIP, port=3306, user=user,\
                                    password=password, db=dbName, charset='utf8')
        print('>> 数据库连接成功.')
        print('>> sql: select * from posts')
        cursor = connection.cursor()
        cursor.execute('select * from posts')
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


if __name__ == '__main__':
    while 1:
        title = input('请输入帖子标题:>')
        publish = input('请输入发帖时间(YYYY-MM-DD):>')
        author = input('请输入作者(默认为"匿名"):>')
        author = '匿名' if author=='' else author
        text = input('请输入帖子内容:>')
        sql = R"insert into posts value(null, '%s', '%s', '%s', '%s') "\
                        %(title, publish, author, text)

        print('影响行数：', addPosts(sql))

        if input('是否继续输入(y/n):>').lower() != 'y':
            result = showPosts()
            for item in result:
                print(item)
            break

