import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Get the bot token from environment variable (we’ll set this in Koyeb)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I’m your bot. How can I help you today?")

# Main function to set up the bot
def main() -> None:
    # Create the Application with the token
    application = Application.builder().token(TOKEN).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot with polling (no webhook setup needed for simplicity)
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
