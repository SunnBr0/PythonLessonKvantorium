import random
from telegram import Update
from telegram.ext import ApplicationBuilder,filters,ContextTypes
from telegram.ext import CommandHandler,MessageHandler
async def startFunc(update: Update,context):
    await update.message.reply_text(f"Введите предложение")
async def stringFunc(update: Update,context):
    strValue = update.message.text
    newValue  = strValue.split(" ")
    resWord = ""
    for item  in newValue:
        resWord+= item[0]
    await update.message.reply_text(f"Слово из первых букв каждого слова : {resWord.lower()}")
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT,stringFunc))
    app.run_polling()
main()