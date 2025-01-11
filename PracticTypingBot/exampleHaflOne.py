import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes


# Определите функцию обратного вызова для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я эхо-бот. Отправьте мне сообщение, и я его повторю.')

# Определите функцию обратного вызова для команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Доступные команды:\n"
        "/start - Начать взаимодействие с ботом\n"
        "/help - Показать это сообщение\n"
        "/text - Отправить текстовое сообщение\n"
        "/photo - Отправить фото\n"
        "/audio - Отправить аудио\n"
        "/contact - Отправить контакт\n"
        "/poll - Отправить опрос\n"
        "/dice - Отправить анимацию броска кубика\n"
        "/chat_action - Отправить действие чата\n"
    )
    await update.message.reply_text(help_text)

# Определите функцию обратного вызова для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Определите функцию обратного вызова для отправки текстового сообщения
async def send_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Это текстовое сообщение.")

# Определите функцию обратного вызова для отправки фото
async def send_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('./test.jpg', 'rb') as photo:
        await update.message.reply_photo(photo)

# Определите функцию обратного вызова для отправки аудио
async def send_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('./test.mp3', 'rb') as audio:
        await update.message.reply_audio(audio)

# Определите функцию обратного вызова для отправки документа
async def send_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('./test.pdf', 'rb') as document:
        await update.message.reply_document(document)

# Определите функцию обратного вызова для отправки контакта
async def send_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_contact(phone_number="+123456789", first_name="Имя", last_name="Фамилия")

# Определите функцию обратного вызова для отправки опроса
async def send_poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_poll(question="Ваш вопрос?", options=["Опция 1", "Опция 2", "Опция 3"])

# Определите функцию обратного вызова для отправки анимации броска кубика
async def send_dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_dice(emoji="🎲")

# Определите функцию обратного вызова для отправки действия чата
async def send_chat_action(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_chat_action(action="typing")


def main() -> None:
    # Вставьте свой токен API
    application = ApplicationBuilder().token("7837855186:AAHkcknjA_dQTHRJcjrTrla0XQlgr2C2qHc").build()

    # Зарегистрируйте обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("text", send_text))
    application.add_handler(CommandHandler("photo", send_photo))
    application.add_handler(CommandHandler("audio", send_audio))
    application.add_handler(CommandHandler("contact", send_contact))
    application.add_handler(CommandHandler("poll", send_poll))
    application.add_handler(CommandHandler("dice", send_dice))
    application.add_handler(CommandHandler("chat_action", send_chat_action))
    application.add_handler(MessageHandler(filters.TEXT , echo))
    # Зарегистрируйте обработчик ошибок
    # Запустите бота
    application.run_polling()

if __name__ == '__main__':
    main()
