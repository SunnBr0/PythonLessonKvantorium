from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram import Update,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from telegram import KeyboardButtonPollType
async def startFunc(update:Update,context):
    arrButton = [
        [KeyboardButton("Создать опрос",request_poll=KeyboardButtonPollType("regular"))]
    ]
    await update.message.reply_text("Выберите кнопку",
        reply_markup=ReplyKeyboardMarkup(arrButton,one_time_keyboard=True)
    )
async def button(update:Update,context):
    if update.message.poll :
         await update.message.reply_text(f"Вы создали опрос:{update.message.poll.question}")
    else:
        await update.message.reply_text(f"Пожалуйста,выберите действие")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT | filters.POLL,button))
    app.run_polling()
main()