import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Определите функцию обратного вызова для команды /start
async def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id
    text = update.message.text
    await update.message.reply_text(f'Привет, {user.first_name}! Вы написали: {text} чат id {chat_id}')

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Сохраните данные в контексте
    context.user_data['key'] = 'value'
    # Получите данные из контекста
    value = context.user_data.get('key')
    await update.message.reply_text(f'Значение: {value}')

# Определите функцию обратного вызова для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

# Определите функцию обратного вызова для обработки ошибок
def main():
    # Вставьте свой токен API
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()

    # Зарегистрируйте обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("test", test))
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.TEXT, echo))

    # Запустите бота
    application.run_polling()

if __name__ == '__main__':
    main()