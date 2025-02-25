from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,KeyboardButtonPollType
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters
async def start(update: Update,context):
    arrButton = [
        [KeyboardButton("Создать опрос",request_poll=KeyboardButtonPollType('regular'))],
        [KeyboardButton("Отправить контакт",request_contact=True)],
        [KeyboardButton('Отправить местоположение', request_location=True)]
    ]
    await update.message.reply_text(
        "Выберите действие:",reply_markup=ReplyKeyboardMarkup(arrButton,one_time_keyboard=True)
    )
async def button(update: Update,context):
    if update.message.poll:
        await update.message.reply_text(f"Вы создали опрос: {update.message.poll.question}")
    elif update.message.contact :
        await update.message.reply_text(f"Вы отправили контакт: {update.message.contact.phone_number}")
    elif update.message.location:
        await update.message.reply_text(f'Место: {update.message.location.latitude}, {update.message.location.longitude}')
    else :
        await update.message.reply_text("Пожалуйста выберите действие")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT,button))
    app.run_polling()
main()