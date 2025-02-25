import random
from telegram import Update
from telegram.ext import ApplicationBuilder,filters,ContextTypes
from telegram.ext import CommandHandler,MessageHandler
words = ["Яблоко","Банан","вишня"]
def scrambledWord(word):
    wordValue = list(word)
    random.shuffle(wordValue)
    resWord = "".join(wordValue)
    return resWord
async def startFunc(update: Update,context:ContextTypes):
    randWord = random.choice(words)
    scrambled = scrambledWord(randWord)
    context.user_data["word"] = randWord
    await update.message.reply_text(f"Угадайте слово: {scrambled}")
async def gameFunc(update: Update,context:ContextTypes):
    userValue = update.message.text.lower()
    correctWord = context.user_data.get("word").lower()
    if  userValue == correctWord:
        await update.message.reply_text("Поздравляю ! вы угадали слово!")
        await startFunc(update,context)

def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT,gameFunc))
    app.run_polling()
main()