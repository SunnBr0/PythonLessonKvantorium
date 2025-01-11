
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   #reply_keyboard = [['1', '2'], ['3', '4'],['3']]
    reply_keyboard = [['1', '2']]
    await update.message.reply_text(
        'Выберите кнопку:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_choice = update.message.text
    await update.message.reply_text(f'Вы нажали {user_choice}')

def main():
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT , button))
    application.run_polling()

main()