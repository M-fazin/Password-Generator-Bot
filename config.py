import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") # Your Bot Token From @BotFather
    APP_ID = int(os.environ.get("APP_ID", 12345))
      # Your APP ID & API_HASH From my.telegram.org
    API_HASH = os.environ.get("API_HASH")
