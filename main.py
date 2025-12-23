from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN

print("🎵 Uraz Müzik Bot BAŞLIYOR...")

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

bot.start()
print("✅ Bot AKTİF!")
run()
print("🔄 Çalışıyor...")
idle()
