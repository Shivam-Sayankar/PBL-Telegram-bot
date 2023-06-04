import os
import telebot
from telebot import types
from credentials import API_TOKEN
from data import MENU, COMPLETE_MENU

# API_TOKEN = os.environ['BOT_TOKEN']

commands = ['start','hello', 'menu', 'help', 'get_price']
buttons = []

help_text = '''
Here are the commands that can help you place your order:
    /start
    /help
    /menu
    /get_price    

'''

canteen_bot = telebot.TeleBot(API_TOKEN)


# menu_button = types.KeyboardButton('Menu')
# help_button = types.KeyboardButton('Help')
# keyboard = types.InlineKeyboardMarkup()
# keyboard.add(menu_button)


@canteen_bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    canteen_bot.reply_to(message, "Hello there! I'm here to help you out with your canteen order ")


@canteen_bot.message_handler(commands=['help'])
def help_command(message):
    canteen_bot.reply_to(message, help_text)



@canteen_bot.message_handler(commands=['menu'])
def show_menu(message):
    # button = types.InlineKeyboardButton('Pani puri', callback_data='Pani Puri')

    # buttons = [types.InlineKeyboardButton(category, callback_data=category) for category in MENU]

    keyboard = types.InlineKeyboardMarkup()

    maggie_button = types.InlineKeyboardButton('Maggie 🍜', callback_data='Maggie')

    pulao_button = types.InlineKeyboardButton('Pulao 🍛', callback_data='Pulao')

    ande_ka_funda_button = types.InlineKeyboardButton('Ande ka funda 🍳', callback_data='Ande ka funda')

    paratha_button = types.InlineKeyboardButton('Paratha 🫓', callback_data='Paratha')

    hot_drink_button = types.InlineKeyboardButton('Hot drink ☕️', callback_data='Hot drink')

    cold_drink_button = types.InlineKeyboardButton('Cold drink 🍹', callback_data='Cold drink')
    
    keyboard.add(maggie_button, pulao_button,) 
    keyboard.add(ande_ka_funda_button, paratha_button,)
    keyboard.add(hot_drink_button, cold_drink_button)

    # canteen_bot.send_message(chat_id=CHAT_ID, text='Here is our menu 👇', reply_markup=keyboard)
    canteen_bot.reply_to(message, text='🔻 Here are the categories in our menu 🔻', reply_markup=keyboard)    


    # canteen_bot.reply_to(message, message.text)

# @canteen_bot.answer_callback_query(callback_query_id=call.id)
@canteen_bot.callback_query_handler(func=lambda call: True)
def show_categories(call):
    global buttons
    global new_keyboard
    # Check if the callback is from an inline button
    if call.message:
        # Check the data of the button that was pressed
        if call.data in MENU:
            # item_button_handler(call)

            canteen_bot.answer_callback_query(callback_query_id=call.id)
            print(f" this is call.data from show categories button, call.data: {call.data}")

            new_keyboard = types.InlineKeyboardMarkup()
            buttons = [types.InlineKeyboardButton(f"{item} | ₹{MENU[call.data][item]}/-", callback_data=item) for item in MENU[call.data] ]

            for button in buttons:
                new_keyboard.add(button)


            canteen_bot.reply_to(call.message, text=f'😋 Items in the category: {call.data} 😋', reply_markup=new_keyboard) 


@canteen_bot.callback_query_handler(func=lambda call: True)
def item_button_handler(call):
    global new_keyboard
    if call.message:
        # Check the data of the button that was pressed

        conditions = [

        call.data in MENU['Maggie'],
        call.data in MENU['Pulao'],
        call.data in MENU['Ande ka funda'],
        call.data in MENU['Paratha'],
        call.data in MENU['Hot drink'],
        call.data in MENU['Cold drink']
    ]
        if any(conditions):
            for button in buttons:
                if call.data == button.callback_data:
                    
                    print(button.callback_data)




@canteen_bot.message_handler(func=lambda msg: True)
def reply_to_all(message):
    if message.text not in commands:
        canteen_bot.reply_to(message, f'Invalid command')
        canteen_bot.reply_to(message, f'{help_text}')


canteen_bot.infinity_polling()