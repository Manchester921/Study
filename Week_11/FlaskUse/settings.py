import os

basedir = os.path.abspath(os.path.dirname(__name__))


class BasicConfig:
    GLOBAL_PARAM = '基本配置类参数'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True




    pass

class DevelopmentConfig(BasicConfig):
    DEBUG = True
    pass

class ProductConfig(BasicConfig):
    DEBUG = False
    pass

config = {
    'default':BasicConfig,
    'development':DevelopmentConfig,
    'product':ProductConfig,
}