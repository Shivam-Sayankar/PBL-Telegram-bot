import telebot
from telebot import types
from data import MENU, COMPLETE_MENU
from credentials import API_TOKEN

# Create a new instance of the telebot.Bot class
canteen_bot = telebot.TeleBot(API_TOKEN)

current_category = ''
item_selected = ''

@canteen_bot.message_handler(commands=['menu'])
def show_menu_categories(message):

    markup = types.ReplyKeyboardMarkup(row_width=2)

    maggie_button = types.KeyboardButton('Maggie 🍜',)# callback_data='Maggie')

    pulao_button = types.KeyboardButton('Pulao 🍛',)# callback_data='Pulao')

    ande_ka_funda_button = types.KeyboardButton('Ande ka funda 🍳',)# callback_data='Ande ka funda')

    paratha_button = types.KeyboardButton('Paratha 🫓',)# callback_data='Paratha')

    hot_drink_button = types.KeyboardButton('Hot drink ☕️',)# callback_data='Hot drink')

    cold_drink_button = types.KeyboardButton('Cold drink 🍹',)# callback_data='Cold drink')

    markup.add(maggie_button, pulao_button,) 
    markup.add(ande_ka_funda_button, paratha_button,)
    markup.add(hot_drink_button, cold_drink_button)

    canteen_bot.reply_to(message, text='🔻 Here are the categories in our menu 🔻', reply_markup=markup) 




@canteen_bot.message_handler(func=lambda msg: True)
def show_menu(message):

    global current_category, item_selected

    user_message = message.text.strip('🍜🍛🍳 🫓☕️🍹')

    current_category = user_message
    # print(category_title)

    items_markup = types.ReplyKeyboardMarkup()

    if user_message in MENU:
        print(f' this is message.strip: {user_message}')
        print(MENU[user_message])


        items = [
            types.KeyboardButton(f'{item}') for item in MENU[user_message]
        ]

        items_markup.add(*items)

        canteen_bot.reply_to(message, text='🔻 Here are the categories in our menu 🔻', reply_markup=items_markup)
    
    elif user_message in COMPLETE_MENU:

        item_selected = user_message

        # items = [
        #     types.KeyboardButton(f'{item}') for item in COMPLETE_MENU[user_message]
        # ]
        canteen_bot.reply_to(message, text=f'{user_message} costs ₹{COMPLETE_MENU[user_message]}/-')

        items = [
            types.KeyboardButton(f'{i}') for i in range(1, 11)
        ]

        items_markup.add(*items)
        canteen_bot.reply_to(message, text=f'How many {user_message}s would you like to order?', reply_markup=items_markup)

    if user_message.isnumeric:
        print(f'do you want to order {user_message} {item_selected}s?')
        print(message.chat.id)



canteen_bot.infinity_polling()