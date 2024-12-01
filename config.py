import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Get database URL from environment variables
    DATABASE_URL = os.getenv('DATABASE_URL')
    SECRET_KEY =os.getenv('SECRET_KEY', 'default_secret_key')


# SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# DATABASE_URI = os.getenv('LOCAL_DATABASE_URL', 'sqlite:///db.sqlite3')
