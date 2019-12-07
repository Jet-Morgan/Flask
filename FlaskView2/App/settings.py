# -*- coding: UTF-8 -*-
def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)


class   Config:

    TESTING = False

    DEBUG = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "Rock"

    SESSION_TYPE = "redis"


class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"000000",
        "HOST":"localhost",
        "PORT":5000,
        "NAME":"GP1FlaskDay02"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = get_db_uri(dbinfo)


class TestingConfig(Config):

    TESTING = True       #此处可能有错，TESTINE可能是TESTING

    dbinfo = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"000000",
        "HOST":"localhost",
        "PORT":5000,
        "NAME":"GP1FlaskDay02"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"000000",
        "HOST":"localhost",
        "PORT":5000,
        "NAME":"GP1FlaskDay02"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "USER":"root",
        "PASSWORD":"000000",
        "HOST":"localhost",
        "PORT":5000,
        "NAME":"GP1FlaskDay02"
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = get_db_uri(dbinfo)


envs = {
    "develop":DevelopConfig,
    "testing":TestingConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}