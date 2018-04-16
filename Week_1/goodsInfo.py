#-*- Coding:utf-8-*-
"""
    goodsInfo.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    列表的应用 类对象的应用
    @author: Manchester
    @data: 2018-04-10 PM
"""

class GoodsInfo:
    def __init__(self, goodsId, name, price):
        self.list = [goodsId, name, price]
        pass

    def info(self):
        print('商品信息：')
        print('\t商品编号：%s\t商品名称：%s\t商品价格：%s元\t' % (self.list[0], self.list[1], self.list[2]))
        pass
    
    def edit(self, index, value):
        self.list[index] = value
        pass
    pass

if __name__ == '__main__':
    apple = GoodsInfo('0001', '苹果', 10 )
    pear = GoodsInfo('0002', '梨子', 8)


    goodsId = 20180411
    count = 1
    locals()['goodsId' + str(count)] = ['0001', '苹果', 10 ]

    print(locals()['goodsId' + str(count)])
    
    asd = GoodsInfo('0003', '苹果2', 15 )

    list1 = []
    list1.append(apple)
    list1.append(pear)
    for i in list1:
        i.info()


    # apple.info()
    # pear.info()
    # apple.edit(2, 11)
    # apple.info()
    # del pear
    # pear.info()
    # pass
