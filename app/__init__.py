from flask import Flask, app
# from config import DevConfig
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

     #Creating app configurations
    app.config.from_object(config_options[config_name])

    #Initializing Flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    

    return app