from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config, Config


db = SQLAlchemy()
celery = Celery(__name__, broker=Config.broker_url)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    celery.conf.update(app.config)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
