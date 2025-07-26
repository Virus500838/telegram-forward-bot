from telegram.ext import ApplicationBuilder, MessageHandler, filters
from config import BOT_TOKEN
from handlers import forward_all

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, forward_all))

if __name__ == "__main__":
    print("🤖 Bot is running...")
    app.run_polling()