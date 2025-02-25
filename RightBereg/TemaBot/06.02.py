from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram import Update,ReplyKeyboardMarkup
async def startFunc(update:Update,context):
    arrButton = [["1","2"],["3","4","5"]]
    await update.message.reply_text("Выберите кнопку",
        reply_markup=ReplyKeyboardMarkup(arrButton,one_time_keyboard=True)
    )
async def button(update:Update,context):
    userChoice = update.message.text
    await update.message.reply_text(f"Вы нажали {userChoice}")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT,button))
    app.run_polling()
main()