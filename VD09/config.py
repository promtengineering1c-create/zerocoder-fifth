import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env_state = os.environ.get('ENV_STATE', 'development')
env_file = f'.env.{env_state}'  
load_dotenv(os.path.join(basedir, env_file))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-dev-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')