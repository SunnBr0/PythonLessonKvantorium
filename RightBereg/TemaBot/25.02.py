from telegram import Update,ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder,CommandHandler
from telegram.ext import MessageHandler,filters
from telegram.ext import ConversationHandler,ContextTypes
async def startFunc(update:Update,context):
    await update.message.reply_text(
        "Привет! Как тебя зовут?",
        reply_markup=ReplyKeyboardRemove()
    )
    return 0
async def getNameFunc(update:Update,context:ContextTypes):
    context.user_data["name"]= update.message.text
    await update.message.reply_text("Сколько вам лет?")
    return 1

async def getAgeFunc(update:Update,context:ContextTypes):
    context.user_data["age"] = update.message.text
    name = context.user_data["name"]
    age = context.user_data["age"]
    await update.message.reply_text(
        f"Привет, {name}!, Вам{age} лет",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
    
async def  cancelFunc(update:Update,context:ContextTypes):
    await update.message.reply_text(
        "Отменено. Если хотите начать сначала ,отправь /start",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def main():
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    convHandler = ConversationHandler(
        entry_points=[CommandHandler("start",startFunc)],
        states={
            0 : [MessageHandler(filters.TEXT,getNameFunc)],
            1 : [MessageHandler(filters.TEXT,getAgeFunc)]
        },
        fallbacks=[CommandHandler("cancel",cancelFunc)]
    )
    app.add_handler(convHandler)
    app.run_polling()

main()