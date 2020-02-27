# -*- Coding:utf-8 -*-
"""
    sqlUse.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    logging应用
    @author: Manchester
    @data: 2018-04-29
"""

import mysqlUse


sql = R"insert into lessor value(null, '%s', '%s', '%s', '%s') "\
        %('usertest02', '123456', '测试用户2', '2018-05-07')
print(mysqlUse.dbExcutrSQL(sql))
        

sql = R"update lessor set lepassword='%s' where leid=%d "%('000000', 5)
print(mysqlUse.dbExcutrSQL(sql))

sql = R"delete from lessor where leid=%d"%(14)
print(mysqlUse.dbExcutrSQL(sql))


sql = R"select * from lessor "

result = mysqlUse.dbQuerySQL(sql)
for item in result:
    print(item)