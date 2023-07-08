import os
import secrets

from dotenv import load_dotenv
class Config(object):
    load_dotenv()
    DB_NAME = os.environ.get('DB_NAME')
    HOST_NAME = os.environ.get('HOST_NAME')
    HOST_PASSWORD = os.environ.get('HOST_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{HOST_PASSWORD}@{HOST_NAME}/{DB_NAME}?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    BOOTSTRAP_BOOTSWATCH_THEME = 'lux'