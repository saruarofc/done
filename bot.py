import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import socketserver

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Simple TCP server for health check
class HealthCheckHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.sendall(b"OK\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I’m your bot. How can I help you today?")

def run_health_server():
    server = socketserver.TCPServer(("0.0.0.0", 8000), HealthCheckHandler)
    server.serve_forever()

async def main() -> None:
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    # Run polling in async loop
    await application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    # Start health check server in a separate thread
    import threading
    threading.Thread(target=run_health_server, daemon=True).start()
    # Run the bot
    asyncio.run(main())
