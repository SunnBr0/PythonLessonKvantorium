from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Пример расписания уроков
schedule = {
    "Понедельник": ["Математика", "Физика", "Химия"],
    "Вторник": ["Литература", "История", "География"],
    "Среда": ["Биология", "Информатика", "Физкультура"],
    "Четверг": ["Английский", "Испанский", "Французский"],
    "Пятница": ["Искусство", "Музыка", "Труд"],
    "Суббота": ["Обществознание", "Экономика", "Право"],
    "Воскресенье": ["Выходной"]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я бот-расписание. Используйте /schedule <день недели>, чтобы узнать расписание.')

async def get_schedule(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        day = context.args[0].capitalize()
        if day in schedule:
            lessons = ", ".join(schedule[day])
            await update.message.reply_text(f'Расписание на {day}: {lessons}')
        else:
            await update.message.reply_text('Неверный день недели. Попробуйте снова.')
    except (IndexError, ValueError):
        await update.message.reply_text('Использование: /schedule <день недели>')

def main():
    token = '7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc'
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('schedule', get_schedule))
    app.run_polling()

if __name__ == '__main__':
    main()