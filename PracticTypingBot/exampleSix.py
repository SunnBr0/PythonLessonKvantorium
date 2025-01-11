from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        [KeyboardButton('Отправить контакт', request_contact=True)],
        [KeyboardButton('Отправить местоположение', request_location=True)]
    ]
    await update.message.reply_text(
        'Выберите действие:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.contact:
        await update.message.reply_text(f'Вы отправили контакт: {update.message.contact.phone_number}')
    elif update.message.location:
        await update.message.reply_text(f'Вы отправили местоположение: {update.message.location.latitude}, {update.message.location.longitude}')
    else:
        await update.message.reply_text('Пожалуйста, выберите действие.')

def main() -> None:
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT | filters.CONTACT | filters.LOCATION, button))
    application.run_polling()

if __name__ == '__main__':
    main()