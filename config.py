class Config(object):
    MERCHANT_ID = "2345678"

class TestEnvironment(Config):
    MERCHANT_ID ="234567898765"
    DBCONN = "Db connection"

class ProductionEnvironment(Config):
    MERCHANT_ID: "abvnnnnn"