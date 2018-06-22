import os
basedir = os.path.abspath(os.path.dirname(__name__))




class BasicConfig:
    GLOBAL_PARAM = '基本配置类参数'
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