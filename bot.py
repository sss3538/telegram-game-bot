import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your GitHub Pages URL
GAME_URL = "https://sss3538.github.io/telegram-game-bot/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with the game web app button."""
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton(
            "🎮 Play Flappy Bird",
            web_app=WebAppInfo(url=GAME_URL)
        )]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!
\n"
        f"🎮 Добро пожаловать в нашу игровую зону!\n\n"
        f"Нажми на кнопку ниже, чтобы играть в Flappy Bird 🐦\n\n"
        f"Удачи! 🍀",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send help message."""
    help_text = """
🎮 *Команды бота:*

/start - Начать игру
/help - Справка
/stats - Твои статистики

📋 *Как играть:*
1️⃣ Нажми на кнопку "Play Flappy Bird"
2️⃣ Кликай или касайся, чтобы управлять птицей
3️⃣ Избегай труб и земли
4️⃣ Собирай очки! ⭐
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send user statistics."""
    user_id = update.effective_user.id
    await update.message.reply_text(
        f"📊 *Твои статистики:*\n\n"
        f"ID пользователя: `{user_id}`\n"
        f"Рекордный результат: Скоро будет отслеживаться\n\n"
        f"Играй больше, чтобы улучшить результат! 🚀",
        parse_mode='Markdown'
    )

def main() -> None:
    """Start the bot."""
    TOKEN = os.getenv('TELEGRAM_TOKEN')
    
    if not TOKEN:
        raise ValueError("❌ TELEGRAM_TOKEN не установлен!")
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stats", stats_command))

    logger.info("🤖 Бот запущен!")
    print("🤖 Бот успешно запущен и ждёт сообщений...")
    application.run_polling()

if __name__ == '__main__':
    main()