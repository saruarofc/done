import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I’m your bot. How can I help you today?")

def main() -> None:
    # Build the application
    application = Application.builder().token(TOKEN).build()
    # Add the /start handler
    application.add_handler(CommandHandler("start", start))
    # Run polling directly (no asyncio.run)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
