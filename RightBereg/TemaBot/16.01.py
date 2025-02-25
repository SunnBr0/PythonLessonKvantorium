from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram import Update
async def start(update,context):
    await update.message.reply_text("Привет,то я пишу")
async def echo(update,context):
    text = update.message.text
    await update.message.reply_text(text)
async def sendPhoto(update,context):
    with open("./img.jpg","rb") as photo:
        await update.message.reply_photo(photo)
async def sendAudio(update,context):
    with open("./audio.mp3","rb") as audio:
        await update.message.reply_audio(audio)
async def sendContact(update:Update,context):
    await update.message.reply_contact(phone_number="+80022",first_name="vova",last_name="Фамиля")
async def sendPoll(update:Update,context):
    await  update.message.reply_poll(question="ваш вопрос?",options=["Ответ1","Ответ","Ответ3"])
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("photo",sendPhoto))
    app.add_handler(CommandHandler("contact",sendContact))
    app.add_handler(CommandHandler("poll",sendPoll))
    app.add_handler(CommandHandler("audio",sendAudio))
    app.add_handler(MessageHandler(filters.TEXT,echo))
    app.run_polling()
main()