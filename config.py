import os


class Config:


    

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://patrick:patrick123@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    # SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")
    


class DevConfig(Config):

    DEBUG = True

config_options = {
    'production':ProdConfig,
    'development':DevConfig
}