import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env_state = os.environ.get('ENV_STATE', 'development')
env_file = f'.env.{env_state}'
load_dotenv(os.path.join(basedir, env_file))

class Config:
        URL = os.environ.get('URL') or "https://quoteslate.vercel.app" + "/api/quotes/random"
