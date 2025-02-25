from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler,ContextTypes
from telegram import Update, ReplyKeyboardMarkup,ReplyKeyboardRemove
async def start(update:Update,context):
    arrButtons = [["1","2","+"],["Отмена"]]
    await update.message.reply_text(
        "Выберите кнопку",
            reply_markup=ReplyKeyboardMarkup(arrButtons,one_time_keyboard=True)
        )
async def button(update:Update,context):
    userChoice = update.message.text
    if userChoice == "Отмена":
        await update.message.reply_text("Действие отменено",reply_markup=ReplyKeyboardRemove())
    else:
        await update.message.reply_text(f"Вы нажали {userChoice}")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT,button))
    app.run_polling()
main()