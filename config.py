class BaseConfig(object):
    DEBUG = False
    SECRET_KEY ='NOTSECUREKEY'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1/pedsqbank'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = 'localhost:5000'