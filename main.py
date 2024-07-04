from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext


TOKEN: Final = '7207956256:AAHkznVB8hJlatz76qm-WwtoxE2-IeByBhc'
BOT_USERNAME: Final = '@SE20_SE20_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! I am SE20 bot, here just for helping you :)")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("plzz just chose subject so that i can help you")


async def subjects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("1.Software Engineering\n 2.AI \n3.Networking")


#Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'i' in processed:
        return 'Remember to df!'
    
    return 'I do not understand what you wrote.....'



async def handle_message(update:Update,context:ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('BOT:',response)
    await update.message.reply_text(response)


async def error(update:Update,context:CallbackContext):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print("Starting bot....")
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('subjects',subjects_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    # Errors
    
    app.add_error_handler(error)

    # Polls the bot 
    print("Polling...")
    app.run_polling(poll_interval=3)

