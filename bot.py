import random
import string
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = "7558676490:AAFz9ES6b0E40MFcHzqJS_wod_XYeUKQ0S0"

def generate_password(length: int = 16) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Type /generate to get a strong password.')

async def generate(update: Update, context: CallbackContext) -> None:
    password = generate_password()
    await update.message.reply_text(f"Your strong password is: {password}")

def main():
    # Create the application object
    application = Application.builder().token(TOKEN).build()

    # Add the handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate", generate))

    # Start polling
    application.run_polling()

if __name__ == '__main__':
    main()
