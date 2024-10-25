import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # App config
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # API Keys
    TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    
    # Ethereum
    DONATION_WALLET = os.getenv('DONATION_WALLET', '0x00fC876d03172279E04CC30E5edCE103c3d23C1A')
