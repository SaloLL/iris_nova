# bot/handlers.py

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from .services import MessageService


class BotHandlers:
    def __init__(self):
        self.message_service = MessageService()

        self.main_menu = ReplyKeyboardMarkup(
            [["📊 Registrar valor"], ["❓ Ayuda"]],
            resize_keyboard=True
        )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Bienvenido 👋\nHola! Soy Iris, estoy aquí para ayudarte con tus finanzas, antes de empezar vamos a LOGEARTE",
            reply_markup=self.main_menu
        )

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        text = update.message.text

        print(f"[USER] {user.id} | {user.username} | {text}")

        result = self.message_service.process_message(text)

        if result["status"] == "success":
            await update.message.reply_text(
                f"✅ Valor registrado: {result['value']}"
            )

        elif result["status"] == "error":
            await update.message.reply_text(result["message"])

        else:
            await update.message.reply_text(
                "No entendí eso."
            )