import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Возможные варианты
options = ["камень", "ножницы", "бумага"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Давай сыграем в "Камень, ножницы, бумага". Введите /play <ваш выбор>.')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        user_choice = context.args[0].lower()
        if user_choice not in options:
            raise ValueError("Неверный выбор.")

        bot_choice = random.choice(options)
        await update.message.reply_text(f'Я выбрал: {bot_choice}')

        if user_choice == bot_choice:
            result = "Ничья!"
        elif (user_choice == "камень" and bot_choice == "ножницы") or \
             (user_choice == "ножницы" and bot_choice == "бумага") or \
             (user_choice == "бумага" and bot_choice == "камень"):
            result = "Вы выиграли!"
        else:
            result = "Вы проиграли!"

        await update.message.reply_text(result)

    except (IndexError, ValueError):
        await update.message.reply_text('Использование: /play <камень|ножницы|бумага>')

def main():
    token = '7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('play', play))
    app.run_polling()

if __name__ == '__main__':
    main()