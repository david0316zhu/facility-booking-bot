"""
Telegram SMU Booking Bot
17 September 2022
Version 0.0.1
This bot helps to book facilities in SMU
"""

import telegram.ext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
BUILDINGS = ("LKCSB", "LKSLIB", "SOA", "SCIS1", "SOE/SCIS2", "SOSS/CIS")
FACILITY = {"LKCSB": ["Classroom", "GSR", "Seminar Room"],
            "LKSLIB": ["Project Room", "Study Booth"], "SOA": ["Classroom", "GSR", "Seminar Room"],
            "SCIS1": ["GSR", "Seminar Room"], "SOE/SCIS2": ["Classroom", "GSR", "Seminar Room"],
            "SOSS/CIS": ["Classroom", "Seminar Room"]}
LEVELS = {"LKCSB Classroom": ["2", "3"], "LKCSB GSR": ["1", "2", "3"], "LKCSB Seminar Room": ["1", "2", "3"],
          "LKSLIB Project Room": ["2", "3", "4", "5"], "LKSLIB Study Booth": ["2", "3", "4"],
          "SOA Classroom": ["2"], "SOA GSR": ["2", "3"], "SOA Seminar Room": ["1", "2", "3"],
          "SCIS1 GSR": ["2", "3"], "SCIS1 Seminar Room": ["2", "3"],
          "SOE/SCIS2 Classroom": ["2", "3", "4"], "SOE/SCIS2 GSR": ["2", "3", "4"], "SOE/SCIS2 Seminar Room": ["B1", "2", "3", "4", "5"],
          "SOSS/CIS Classroom": ["1", "3"], "SOSS/CIS Seminar Room": ["B1", "1", "2", "3"]}

ROOMS = {"LKCSB Classroom 2": ["2-1"], "LKCSB Classroom 3": ["3-2", "3-3", "3-4", "3-5"],
         "LKCSB GSR 1": ["1-1", "1-2"],
         "LKCSB GSR 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8", "2-9", "2-10",
                         "2-11", "2-12", "2-13", "2-14", "2-15", "2-16", "2-17", "2-18", "2-19",
                         "2-20", "2-21", "2-22", "2-23", "2-24", "2-25"],
         "LKCSB GSR 3": ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10",
                         "3-11", "3-12", "3-13", "3-14", "3-15", "3-16", "3-17", "3-18", "3-19",
                         "3-20", "3-21", "3-22", "3-23", "3-24", "3-25", "3-26", "3-27", "3-28", "3-29", "3-30",
                         "3-31", "3-32", "3-33", "3-34", "3-35"],
         "LKCSB Seminar Room 1": ["1-1", "1-2"], "LKCSB Seminar Room 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8"],
         "LKCSB Seminar Room 3": ["3-1", "3-2", "3-3",  "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10"],
         "LKSLIB Project Room 2": ["2-0", "2-1", "2-2", "2-3", "2-3", "2-4", "2-5"], "LKSLIB Project Room 3": ["3-1", "3-2", "3-3", "3-4", "3-5"],
         "LKSLIB Project Room 4": ["4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7", "4-8", "4-9", "4-10",
                                   "4-11", "4-12", "4-13", "4-14", "4-15", "4-16", "4-17", "4-18"],
         "LKSLIB Project Room 5": ["5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7"], "LKSLIB Study Booth 2": ["2-1", "2-2", "2-3", "2-4", "2-5"],
         "LKSLIB Study Booth 3": ["3-1"], "LKSLIB Study Booth 4": ["4-1", "4-2", "4-3"],
         "SOA Classroom 2": [2-1], "SOA GSR 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8", "2-9"],
         "SOA GSR 3": ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10"],
         "SOA Seminar Room 1": ["1-1", "1-2", "1-3"], "SOA Seminar Room 2": ["2-1", "2-2", "2-3", "2-4", "2-5"], "SOA Seminar Room 3": ["3-1", "3-2", "3-3",  "3-4", "3-5"],
         "SCIS1 GSR 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7"], "SCIS1 GSR 3": ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6"],
         "SCIS1 Seminar Room 2": ["2-1", "2-2", "2-3", "2-4"], "SCIS1 Seminar Room 3": ["3-1", "3-2", "3-3",  "3-4"],
         "SOE/SCIS2 Classroom 2": ["2-1", "2-2"], "SOE/SCIS2 Classroom 3": ["3-1", "3-2", "3-3",  "3-4", "3-5"], "SOE/SCIS2 Classroom 4": ["4-1", "4-3"],
         "SOE/SCIS2 GSR 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8", "2-9", "2-10",
                             "2-11", "2-12", "2-13", "2-14", "2-15", "2-16", "2-17"],
         "SOE/SCIS2 GSR 3": ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10",
                             "3-11", "3-12", "3-13", "3-14", "3-15", "3-16", "3-17", "3-18"],
         "SOE/SCIS2 GSR 4": ["4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7", "4-8", "4-9"],
         "SOE/SCIS2 Seminar Room 2": ["2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7", "2-8", "2-9", "2-10"],
         "SOE/SCIS2 Seminar Room 3": ["3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-10"],
         "SOE/SCIS2 Seminar Room 4": ["4-1", "4-2", "4-3", "4-4"], "SOE/SCIS2 Seminar Room 5": ["5-1", "5-2"],
         "SOE/SCIS2 Seminar Room B1": ["B1-1", "B1-2"], 
         "SOSS/CIS Classroom 1": ["1-2"], "SOSS/CIS Classroom 3": ["3-2", "3-3", "3-4", "3-5"], "SOSS/CIS Seminar Room 1": ["1-1", "1-3"],
         "SOSS/CIS Seminar Room 2": ["2-1", "2-2"], "SOSS/CIS Seminar Room 3": ["3-1", "3-3"], "SOSS/CIS Seminar Room B1": ["B1-1"]
         }



updater = telegram.ext.Updater("", use_context=True)
disp = updater.dispatcher
building_selection = None
facility_selection = None
level_selection = None
room_selection = None
date_selection = None
def options(update, context):
    button = []
    for option in BUILDINGS:
        button.append([InlineKeyboardButton(option, callback_data=option)])
    markup = InlineKeyboardMarkup(button)
    print(markup)
    update.message.reply_text(text="Please choose a building", reply_markup=markup)
    


def button(update, context):
    try:
        global building_selection
        global facility_selection
        global level_selection
        global room_selection
        global date_selection
        choice = update.callback_query.data
        print(choice)
        if choice in BUILDINGS:
            building_selection = choice
            button = []
            facil_li = FACILITY.get(building_selection)
            if not facil_li:
                raise Exception
            for option in facil_li:
                button.append([InlineKeyboardButton(option, callback_data=option)])
            markup = InlineKeyboardMarkup(button)
            print(markup)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a facility type", reply_markup=markup)
        elif choice in FACILITY[building_selection]:
            facility_selection = choice
            build_facil = building_selection + " " + facility_selection
            button = []
            levels = LEVELS.get(build_facil)
            if not levels:
                raise Exception
            for option in levels:
                button.append([InlineKeyboardButton(option, callback_data=option)])
            markup = InlineKeyboardMarkup(button)
            print(markup)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a level", reply_markup=markup)
        elif choice in LEVELS[building_selection + " " + facility_selection]:
            level_selection = choice
            build_lvl = building_selection + " " + facility_selection + " " + level_selection
            print(build_lvl)
            button = []
            rooms = ROOMS.get(build_lvl)
            if not rooms:
                raise Exception
            for option in rooms:
                button.append([InlineKeyboardButton(option, callback_data=option)])
            markup = InlineKeyboardMarkup(button)
            print(markup)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose a room", reply_markup=markup)

        elif building_selection and facility_selection and level_selection and not room_selection:
            room_selection = choice
            if not date_selection:
                context.bot.send_message(chat_id=update.effective_chat.id, text="Please key in the dates")
            
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Building not found")

def date_select(update, context):
    if building_selection and facility_selection and level_selection and room_selection and not date_selection:
        print(update.message.text)




disp.add_handler(telegram.ext.CommandHandler("option", options))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, date_select))

disp.add_handler(telegram.ext.CallbackQueryHandler(button))
updater.start_polling()
updater.idle()