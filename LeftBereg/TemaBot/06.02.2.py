from telegram import Update
from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler,MessageHandler
async def startFunc(update: Update , context):
    await update.message.reply_text(
        "Привет,я бот калькулятор.Введите 5 + 2 и получите ответ"
    )
async def caclulate(update: Update , context):
    strValue = update.message.text
    valueOne,oper,valueTwo = strValue.split()
    valueOne = float(valueOne)
    valueTwo = float(valueTwo)
    if oper == "+":
        res = valueOne+ valueTwo
    elif oper == "-":
        res = valueOne+ valueTwo
    await update.message.reply_text(f"Результат {res}")
def main(): 
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start",startFunc))
    app.add_handler(MessageHandler(filters.TEXT,caclulate))
    app.run_polling()
main()