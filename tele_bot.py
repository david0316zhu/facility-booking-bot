"""
Telegram SMU Booking Bot
17 September 2022
Version 0.0.1
This bot helps to book facilities in SMU
"""

import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = telegram.ext.Updater("", use_context=True)
disp = updater.dispatcher

def options(update, context):
    button = [
        [InlineKeyboardButton("Choice 1", callback_data="choice 1")],
        [InlineKeyboardButton("Choice 2", callback_data="choice 2")]
    ]
    markup = InlineKeyboardMarkup(button)
    print(markup)
    update.message.reply_text(text="Please choose an option", reply_markup=markup)
    


def button(update, context):
    choice = update.callback_query.data
    if choice == "choice 1":
        button = [
        [InlineKeyboardButton("location1", callback_data="loc 1")],
        [InlineKeyboardButton("location1", callback_data="loc 2")]
        ]
        markup = InlineKeyboardMarkup(button)
        print(markup)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an option", reply_markup=markup)
        
    




disp.add_handler(telegram.ext.CommandHandler("option", options))


disp.add_handler(telegram.ext.CallbackQueryHandler(button))
updater.start_polling()
updater.idle()