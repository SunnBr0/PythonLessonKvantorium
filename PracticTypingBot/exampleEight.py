from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters, ContextTypes

# Состояния для ConversationHandler
NUM1, NUM2, OPERATION = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Привет! Я бот-калькулятор. Введите первое число:"
    )
    return NUM1

async def num1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    context.user_data['num1'] = float(update.message.text)
    await update.message.reply_text(
        f"Спасибо, {user.first_name}! Теперь введите второе число:"
    )
    return NUM2

async def num2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data['num2'] = float(update.message.text)
    await update.message.reply_text(
        "Теперь введите операцию (+, -, *, /):"
    )
    return OPERATION

async def operation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    num1 = context.user_data['num1']
    num2 = context.user_data['num2']
    operation = update.message.text

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            await update.message.reply_text("Ошибка: деление на ноль!")
            return ConversationHandler.END
    else:
        await update.message.reply_text("Ошибка: неверная операция!")
        return ConversationHandler.END

    await update.message.reply_text(f"Результат: {result}")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Операция отменена. Введите /start, чтобы начать сначала.",
        reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END

def main() -> None:
    application = ApplicationBuilder().token('7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NUM1: [MessageHandler(filters.TEXT , num1)],
            NUM2: [MessageHandler(filters.TEXT , num2)],
            OPERATION: [MessageHandler(filters.TEXT , operation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
