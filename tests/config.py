from config import BaseConfig


class TestBaseConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY ='NOTSECUREKEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'