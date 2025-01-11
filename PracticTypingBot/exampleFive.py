from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [
        [KeyboardButton('Создать опрос', request_poll=KeyboardButtonPollType('regular'))]
    ]
    await update.message.reply_text(
        'Выберите действие:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.poll:
        await update.message.reply_text(f'Вы создали опрос: {update.message.poll.question}')
    else:
        await update.message.reply_text('Пожалуйста, выберите действие.')

def main() -> None:
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT | filters.POLL, button))
    application.run_polling()

if __name__ == '__main__':
    main()