import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# Define function to handle "/start" command
def start(update, context):
    # Send welcome message
    update.message.reply_text("Welcome to the image format converter bot!\nPlease select the format you want to convert your image to:")

    # Create inline keyboard with image format options
    keyboard = [[InlineKeyboardButton("JPEG", callback_data='JPEG'),
                 InlineKeyboardButton("PNG", callback_data='PNG'),
                 InlineKeyboardButton("BMP", callback_data='BMP'),
                 InlineKeyboardButton("GIF", callback_data='GIF')]]

    # Add keyboard to message
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please select:', reply_markup=reply_markup)

# Define function to handle callback query
def button(update, context):
    query = update.callback_query
    query.answer()

    # Get image file from message
    message = query.message
    file = message.photo[-1].file_id

    # Get selected image format from callback query
    image_format = query.data

    # Convert image to selected format
    file = context.bot.get_file(file)
    new_file = file.download_as_bytearray()
    new_file = Image.open(io.BytesIO(new_file))
    new_file.format = image_format

    # Send converted image to user
    context.bot.send_photo(chat_id=query.message.chat_id, photo=new_file)

# Define main function to start the bot
def main():
    # Set up bot and token
    updater = Updater("6236372190:AAG_JLHOdgVoaC7xtvtuUuMINERG2-wOuUM", use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
