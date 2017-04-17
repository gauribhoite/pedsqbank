class BaseConfig(object):
    DEBUG = False
    SECRET_KEY ='NOTSECUREKEY'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1/questions'
    SQLALCHEMY_TRACK_MODIFICATIONS = False