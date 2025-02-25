from telegram import Update,ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder,filters
from telegram.ext import CommandHandler,ConversationHandler
from telegram.ext import ContextTypes,MessageHandler
async def startFunc(update: Update,context):
    await update.message.reply_text(
        "Привет! как вас зовут?",
        reply_markup=ReplyKeyboardRemove()
    )
    return 0
async def getName(update: Update,context:ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Сколько вам лет?")
    return 1
async def getAge(update: Update,context:ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text
    name  = context.user_data["name"] 
    age  = context.user_data["age"] 
    await update.message.reply_text(
        f"Привет, {name}! Вам {age } лет",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
async def cancelFunc(update: Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Отмененно.Если хотите начать сначала,отправ /start",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END
def main(): 
    token = "7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc"
    app = ApplicationBuilder().token(token).build()
    arrHandler = ConversationHandler(
        entry_points=[CommandHandler("start",startFunc)],
        states={
            0 : [MessageHandler(filters.TEXT,getName)],
            1: [MessageHandler(filters.TEXT,getAge)]
        },
        fallbacks=[CommandHandler("cancel",cancelFunc)]
    )
    app.add_handler(arrHandler)
    app.run_polling()
main()