class Config(object):
    MYSQL_DATABASE_USER = 'AAA'
    MYSQL_DATABASE_PASSWORD = 'BBB'
    MYSQL_DATABASE_DB = 'AAA'
    MYSQL_DATABASE_HOST = 'sql9.freemysqlhosting.net'

# XXX.pythonanywhere.com
class ProductionConfig(Config):
    ENV = "Prod"

    MYSQL_DATABASE_USER = 'XXX'
    MYSQL_DATABASE_PASSWORD = 'YYY'
    MYSQL_DATABASE_DB = 'XXX$default'
    MYSQL_DATABASE_HOST = 'XXX.mysql.pythonanywhere-services.com'

# 127.0.0.1:5000
class DevelopmentConfig(Config):
    ENV = "Dev"