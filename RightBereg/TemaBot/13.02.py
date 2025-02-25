from telegram import Update,ReplyKeyboardMarkup,KeyboardButton
from telegram.ext import ApplicationBuilder,CommandHandler
from telegram.ext import MessageHandler,filters,ContextTypes
async def startFunc(update: Update, context):
    arrButton = [
        [KeyboardButton("Отправить контакт",request_contact=True)],
        [KeyboardButton("Отправить местоположение",request_location=True)]
    ]
    await update.message.reply_text(
        "Выберите действие",
        reply_markup=ReplyKeyboardMarkup(arrButton,one_time_keyboard=True)
    )
async def button(update: Update, context):
    contactValue = update.message.contact
    locationValue = update.message.location
    if contactValue:
        await update.message.reply_text(f"Вы отправили контакт:{contactValue.phone_number}")
    elif locationValue:
        await update.message.reply_text(f"Местоположение:{locationValue.latitude},{locationValue.longitude}")
    else:
        await update.message.reply_text("Выберите действие")
def main():
    token= "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT | filters.CONTACT| filters.LOCATION,button))
    app.run_polling()
main()