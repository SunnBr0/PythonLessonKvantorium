from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Определите состояния разговора
GET_NAME, GET_AGE = range(2)
# Функция обратного вызова для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Привет! Как вас зовут?",
        reply_markup=ReplyKeyboardRemove()
    )
    return GET_NAME

# Функция обратного вызова для получения имени
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Сколько вам лет?")
    return GET_AGE

# Функция обратного вызова для получения возраста
async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['age'] = update.message.text
    name = context.user_data['name']
    age = context.user_data['age']
    await update.message.reply_text(
        f"Привет, {name}! Вам {age} лет.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

# Функция обратного вызова для команды /cancel
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        'Отменено. Если хотите начать сначала, отправьте /start.',
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def main() -> None:
    # Вставьте свой токен API
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()
    # Определите обработчик разговора
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            GET_NAME: [MessageHandler(filters.TEXT , get_name)],
            GET_AGE: [MessageHandler(filters.TEXT , get_age)]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    application.add_handler(conv_handler)

    # Запустите бота
    application.run_polling()

if __name__ == '__main__':
    main()