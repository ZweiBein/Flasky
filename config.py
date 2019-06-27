import os
from decouple import config as env_config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = env_config('SECRET_KEY', default='very secret string')
    MAIL_SERVER = env_config('MAIL_SERVER', default='smtp.googlemail.com')
    MAIL_PORT = env_config('MAILPORT', default=587)
    MAIL_USE_TLS = env_config(
        'MAIL_USE_TLS', default='true').lower() in ('true', 'on', '1')
    MAIL_USERNAME = env_config('MAIL_USERNAME')
    MAIL_PASSWORD = env_config('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = env_config('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env_config(
        'DEV_DATABASE_URL', default='sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env_config(
        'TEST_DATABASE_URL', default='sqlite://')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = env_config(
        'DATABASE_URL', default='sqlite:///' + os.path.join(basedir, 'data.sqlite'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig,
    'default': DevelopmentConfig
}
