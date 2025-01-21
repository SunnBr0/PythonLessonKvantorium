from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler,ContextTypes
from telegram import Update
async def funcStart (update: Update,context):
    context.user_data["one"] = "one"
    user = update.message.from_user
    chatID = update.message.chat_id
    text = update.message.text
    strText = f"Прив, {user.first_name}!вы написали: {text} чат id{chatID}"
    await update.message.reply_text(f"{strText}")
async def funcTest(update: Update,context:ContextTypes):
    context.user_data["key"] = "value"
    itemValue = context.user_data.get("key")
    itemValueOne = context.user_data.get("one")
    await update.message.reply_text(f"Значение {itemValue} и {itemValueOne}")
async def funcSticker(update: Update,context:ContextTypes):
    idSticker = "CAACAgIAAxkBAAENjPpnj6nVRZ82fL7dgg8iITMiLOHM6gACL2kAAtiPkUkdjJm-PRqfYzYE"
    await update.message.reply_text("это 😁")
    await update.message.reply_sticker(idSticker)
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",funcStart))
    app.add_handler(CommandHandler("test",funcTest))
    app.add_handler(CommandHandler("sticker",funcSticker))
    app.run_polling()
main()