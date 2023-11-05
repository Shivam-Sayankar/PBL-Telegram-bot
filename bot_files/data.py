
MENU = {

    'Maggie' : {

        'Plain maggie' : 30,
        'Masala maggie' : 45,
        'Butter maggie' : 40,
        'Schezwan maggie' : 40,
        'Anda maggie' : 50,
        'Anda schezwan maggie' : 60,
        'Extra cheese' : 20,
    },


    'Pulao' : {

        'Veg pulao' : 60,
        'Paneer pulao' : 80,
        'Mashroom pulao' : 100,
        'Green peas'  : 60,
        'Daal khichadi' : 60,
        'Butter daal khichadi' : 70,
        'Curd rice' : 80,
        'Extra cheese' : 20,
    },


    'Ande ka funda' : {

        'Plain omelet' : 40,
        'Bun omelet' : 50,
        'Bread omelet ': 50,
        'Half fry': 40,
        'French toast': 50,
        'Egg bhurji' : 50,
        'Anda rice' : 60,
        'Boiled fry' : 50,
        'Boiled (2 peices)' : 20,
        'Extra pav' : 10,
        'Extra cheese' : 20,
    },


    'Paratha' : {

        'Aaloo Paratha' : 50,
        'Paneer Paratha' : 70,
        'Gobi Paratha' : 50,
        'Methi Paratha' : 60,
        'Green Peas Paratha' : 50,
        'Mix Veg Paratha' : 70,
        'Laccha Paratha' : 30,
        'Cheese Paratha' : 60,
        'Chole Bhature' : 100,
    },


    'Hot drink' : {

        'Hot Coffee' : 15,
        'Hot Chocolate' : 40,
        'Hot Bornvita' : 35,
        'Hot Milk' : 20,
        'Hot Turmeric Milk' : 35
    },


    'Cold drink' : {

        'Cold coffee ' : 25,
        'Cold bornvita' : 40,
        'Thick coffee ' : 40,
        'Lassi' : 30,
        'Nimbu pani' : 20,
        'Chhach/Taak' : 25
    }

}


COMPLETE_MENU = {}

for category in MENU:
    for item in MENU[category]:
        COMPLETE_MENU.update({item:MENU[category][item]})

