# bot/bot_app.py

import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from .handlers import BotHandlers
from .database import DatabaseManager

class BotApplication:

    def __init__(self):
        load_dotenv()
        self.token = os.getenv("BOT_TOKEN")

        if not self.token:
            raise ValueError("BOT_TOKEN no está definido")

        self.db = DatabaseManager()

        self.app = ApplicationBuilder().token(self.token).build()
        self.handlers = BotHandlers()

        self._register_handlers()

    def _register_handlers(self):
        self.app.add_handler(CommandHandler("start", self.handlers.start))
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self.handlers.handle_message)
        )

    def run(self):
        print("IRIS NOVA iniciado...")
        self.app.run_polling()