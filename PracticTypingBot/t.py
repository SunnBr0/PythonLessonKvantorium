import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Список слов для игры
words = ["олень","питон"]

# Функция для перемешивания букв в слове
def scramble_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Функция для начала игры
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    word = random.choice(words)
    scrambled = scramble_word(word)
    context.user_data['word'] = word
    await update.message.reply_text(f"Угадайте слово: {scrambled}")

# Функция для проверки ответа пользователя
async def guess(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_guess = update.message.text.lower()
    correct_word = context.user_data.get('word', '')
    if user_guess == correct_word:
        await update.message.reply_text("Поздравляю! Вы угадали слово!")
        await start(update, context)  # Начинаем новую игру
    else:
        await update.message.reply_text("Неправильно, попробуйте еще раз!")

# Основная функция для запуска бота
def main() -> None:
    # Вставьте сюда свой токен API
    application = ApplicationBuilder().token('7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, guess))

    application.run_polling()

if __name__ == '__main__':
    main()
