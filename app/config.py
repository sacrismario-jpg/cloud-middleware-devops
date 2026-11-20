class Config:
    TESTING = False
    DEBUG = False

class TestingConfig(Config):
    TESTING = True

class DevelopmentConfig(Config):
    DEBUG = True
