from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
async def start(update,context):
    await update.message.reply_text("Привет,то я пишу")
async def echo(update,context):
    text = update.message.text
    await update.message.reply_text(text)
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT,echo))
    app.run_polling()
main()