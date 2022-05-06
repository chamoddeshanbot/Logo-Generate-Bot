from pyrogram import Client
from config import Config

app = Client(
  "bot",
  bot_token = Config.BOT_TOKEN,
  api_id = Config.API_ID,
  api_hash = Config.API_HASH
)

print("[INFO]: STARTING BOT...")
app.start()
