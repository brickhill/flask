import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    load_dotenv()
    print("IN CONFIG.....")
    print(os.getenv('DOMAIN'))
    print(os.getenv('DATABASE_URL'))
    print("CONFIG2")
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a load of rubbish"

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
