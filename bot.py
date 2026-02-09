import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Welcome! Click the link to play the Web App game: https://your-web-app-link.com')

if __name__ == '__main__':
    TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler('start', start))

    application.run_polling()