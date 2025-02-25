from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler,ContextTypes
from telegram import Update, ReplyKeyboardMarkup
async def start(update:Update,context):
    arrButtons = [["1","2"],["3","4"],["5"]]
    await update.message.reply_text(
        "Выберите кнопку",
            reply_markup=ReplyKeyboardMarkup(arrButtons,one_time_keyboard=True)
        )
async def button(update:Update,context):
    userChoice = update.message.text
    await update.message.reply_text(f"Вы нажали это: {userChoice}")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT,button))
    app.run_polling()
main()