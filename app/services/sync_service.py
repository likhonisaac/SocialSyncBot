import tweepy
import telegram
from config import Config

class SyncService:
    def __init__(self):
        self._init_platforms()
    
    def _init_platforms(self):
        # Twitter setup
        auth = tweepy.OAuthHandler(
            Config.TWITTER_CONSUMER_KEY,
            Config.TWITTER_CONSUMER_SECRET
        )
        self.twitter = tweepy.API(auth)
        
        # Telegram setup
        self.telegram = telegram.Bot(token=Config.TELEGRAM_BOT_TOKEN)
    
    def sync_post(self, content, platforms=None):
        if platforms is None:
            platforms = ['twitter', 'telegram']
        
        results = {}
        
        if 'twitter' in platforms:
            try:
                tweet = self.twitter.update_status(content)
                results['twitter'] = {
                    'success': True,
                    'post_id': tweet.id
                }
            except Exception as e:
                results['twitter'] = {
                    'success': False,
                    'error': str(e)
                }
        
        if 'telegram' in platforms:
            try:
                msg = self.telegram.send_message(
                    chat_id=Config.TELEGRAM_CHANNEL_ID,
                    text=content
                )
                results['telegram'] = {
                    'success': True,
                    'message_id': msg.message_id
                }
            except Exception as e:
                results['telegram'] = {
                    'success': False,
                    'error': str(e)
                }
        
        return results
