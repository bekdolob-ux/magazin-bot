import os
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ.get("8927149628:AAFocJ9JanGi52rxLCHCz_l7l-q4ftespUo")

# TOKEN текшерүү
if not TOKEN:
    print("❌ TOKEN табылган жок!")
    sys.exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Бот иштеп жатат!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
