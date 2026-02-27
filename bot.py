import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Бот иштеп жатат!")

def main():
    if not TOKEN:
        print("❌ TOKEN табылган жок!")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("🚀 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
