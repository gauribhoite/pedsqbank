from config import BaseConfig


class TestBaseConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY ='NOTSECUREKEY'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1/pedsqbank_test'
    SERVER_NAME = 'localhost:5000'