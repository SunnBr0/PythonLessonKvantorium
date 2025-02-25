from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот-калькулятор. Введите выражение в формате "число операция число". Например: 5 + 3')
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # try:
        expression = update.message.text
        num1, operation, num2 = expression.split()
        num1 = float(num1)
        num2 = float(num2)

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
                return
        else:
            await update.message.reply_text("Ошибка: неверная операция!")
            return

        await update.message.reply_text(f"Результат: {result}")

    # except (ValueError, IndexError):
    #     await update.message.reply_text("Ошибка: введите корректное выражение в формате 'число операция число'. Например: 5 + 3")

def main() -> None:
    application = ApplicationBuilder().token('7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT , calculate))
    application.run_polling()

if __name__ == '__main__':
    main()
