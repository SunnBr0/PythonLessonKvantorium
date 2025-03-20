import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Возможные варианты
options = ["камень", "ножницы", "бумага"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Давай сыграем в "Камень, ножницы, бумага". Просто напишите "камень", "ножницы" или "бумага".')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_choice = update.message.text.lower()
    if user_choice not in options:
        await update.message.reply_text('Пожалуйста, выберите "камень", "ножницы" или "бумага".')
        return

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

def main():
    token = '7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, play))
    app.run_polling()

if __name__ == '__main__':
    main()