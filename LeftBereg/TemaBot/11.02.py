from telegram import Update,ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder,CommandHandler
from telegram.ext import ConversationHandler,MessageHandler
from telegram.ext import filters

async def startFunc(update:Update,context):
    await update.message.reply_text(
        "Привет! Я бот калькулятор.Введите первое число: "
    )
    return  0
async def numOneFunc(update:Update,context):
    userName = update.message.from_user
    context.user_data["numOne"] = float(update.message.text)
    await update.message.reply_text(
        f"Спасисбо, {userName.first_name}! Введите второе число"
    )
    return 1
async def numTwoFunc(update:Update,context):
    context.user_data["numTwo"] = float(update.message.text)
    await update.message.reply_text(
        f"Введите операцияю (+,-,*,/)"
    )
    return 2
async def operFunc(update:Update,context):
    numOne  = context.user_data["numOne"]
    numTwo  = context.user_data["numTwo"]
    operValue = update.message.text
    if operValue == "+":
        result = numOne + numTwo
    elif operValue == "-":
        result = numOne - numTwo
    elif operValue == "*":
        result = numOne * numTwo
    elif operValue == "/":
        if numTwo != 0:
            result = numOne/numTwo
        else:
            await update.message.reply_text("Ошибка на ноль")
            return ConversationHandler.END
    else: 
        await update.message.reply_text("Ошибка операция")
        return ConversationHandler.END
    await update.message.reply_text(f"Результат  {result}")
    return ConversationHandler.END
async def cancelFunc(update:Update,context):
    await update.message.reply_text(
        "Операция отменена.  /start , сначала.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    handlers = ConversationHandler(
        entry_points=[CommandHandler("start",startFunc)],
        states={
            0 : [MessageHandler(filters.TEXT,numOneFunc)],
            1 : [MessageHandler(filters.TEXT,numTwoFunc)],
            2 : [MessageHandler(filters.TEXT,operFunc)]
        },
        fallbacks=[CommandHandler("cancel",cancelFunc)]
    )
    app.add_handler(handlers)
    app.run_polling()
main()