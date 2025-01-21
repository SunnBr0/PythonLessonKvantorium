from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram import Update
async def sendAudio(update,context):
    with open("./audio.mp3","rb") as audio:
        await update.message.reply_audio(audio)
async def sendPhoto(update,context):
    with open("./imgCat.webp","rb") as photo:
        await update.message.reply_photo(photo)
async def start(update,context):
    await update.message.reply_text("Привет! я вас знаю")
async def echo(update,context):
    text = update.message.text
    await update.message.reply_text(text)
async def sendContact(update: Update,context):
    await update.message.reply_contact(phone_number="+79558882233",first_name="Имя",last_name="Фамилия")
async def sendPoll(update: Update,context):
    await update.message.reply_poll(question="Ваш вопрос?", options=["Ответ1","Ответ2","Ответ3"])
async def sendSticker(update: Update,context):
    await update.message.reply_dice(emoji="🎲")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(CommandHandler("photo",sendPhoto))
    app.add_handler(CommandHandler("audio",sendAudio))
    app.add_handler(CommandHandler("contact",sendContact))
    app.add_handler(CommandHandler("poll",sendPoll))
    app.add_handler(CommandHandler("sticker",sendSticker))
    app.add_handler(MessageHandler(filters.TEXT,echo))
    app.run_polling()
main()