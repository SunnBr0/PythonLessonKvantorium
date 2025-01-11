from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Функция обратного вызова для команды /start
async def start(update, context):
    await update.message.reply_text('Привет! Что пишете, то я пишу.')
# Функция обратного вызова для обработки текстовых сообщений
async def echo(update, context):
    await update.message.reply_text(update.message.text)
# Основная функция для запуска бота
def main():
    # Вставьте свой токен API
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()
    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT, echo))
    # Запускаем бота
    application.run_polling()

main()