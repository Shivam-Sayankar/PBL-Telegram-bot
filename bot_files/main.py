import telebot
from telebot import types
from data import MENU, COMPLETE_MENU
from credentials import API_TOKEN
import json
import time

# Create a new instance of the telebot.Bot class
canteen_bot = telebot.TeleBot(API_TOKEN)

current_category = ''
item_selected = ''
user_order_details = {}
order_placed = False

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

    global item_selected, user_order_details

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

        canteen_bot.reply_to(message, text=f'{user_message} costs ₹{COMPLETE_MENU[user_message]}/-')

        items = [
            types.KeyboardButton(f'{i}') for i in range(1, 11)
        ]

        items_markup.add(*items)
        canteen_bot.reply_to(message, text=f'How many {user_message}s would you like to order?', reply_markup=items_markup)

    elif user_message.isnumeric:

        num_of_items = int(user_message)

        print(f'do you want to order {user_message} {item_selected}s?')
        print(message.chat.id)
        print(message.chat.username)

        canteen_bot.reply_to(message, text=f'Do you want to add more items?')
        canteen_bot.reply_to(message, text=f'Or is this your final order?')

        items = [
            types.KeyboardButton('Add more items'),
            types.KeyboardButton('This is my final order'),
        ]
    
        items_markup.add(*items)
        canteen_bot.reply_to(message, text=f'What would like to do?', reply_markup=items_markup)

        user_order_details = {
            time.time(): {
                'chat_id': message.chat.id,
                'dish' : item_selected,
                'number_of_dishes': num_of_items,
            }
        }

        print(f"{num_of_items} * {COMPLETE_MENU[item_selected]} {num_of_items*COMPLETE_MENU[item_selected]}")
        
        '''with open('order_details.json', 'a+') as file:
            try:
                # data = json.load(file)
                # print(data)
                json.dump(user_order_details, file, indent=4)
                data = json.load(file)
                data.update(user_order_details)

            except Exception as e:
                print(e)
'''

        try:
            with open("order_details.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("order_details.json", "w") as data_file:
                # Saving updated data
                json.dump(user_order_details, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(user_order_details)

            with open('order_details.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            pass


    elif user_message == 'Add more items':
        show_menu(message)
        pass

    elif user_message == 'This is my final order':
        print(f'your final bill is:\
              {num_of_items}')




canteen_bot.polling()