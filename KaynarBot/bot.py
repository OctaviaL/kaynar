import telebot
from my_token import token
from parsing import main
from telebot import types

bot = telebot.TeleBot(token)
inline_keyboard = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton("Dogs")
btn2 = types.KeyboardButton("Cats")

income_keyboard = types.ReplyKeyboardMarkup()
k1 = types.KeyboardButton('Dogs')
k2 = types.KeyboardButton('Cats')
k3 = types.KeyboardButton('Quit')

inline_keyboard.add(btn1,btn2)
income_keyboard.add(k1,k2)

@bot.message_handler(commands=['start'])
def start(message):
    post = main()
    

    bot.send_message(message.chat.id,"Привет!!Добро пожаловать в Кайнар!")
    
    if len(post) == 0:
        bot.send_message(message.chat.id,"У нас пока нет новых друзей!!")

    # c = 0
    # for i in post:
    #     c += 1
    #     bot.send_message(message.chat.id, str(c) + '. ' + i[0]) 

    bot.send_message(message.chat.id, "Какую новость показать подробней? ", reply_markup=inline_keyboard)
    bot.register_next_step_handler(message, check_answer, post)

def check_answer(message, data):
    number = int(message.text) 
    if number >= len(data):      
        bot.send_message(message.chat.id,"таких новостей пока нет")
        return
    
    
    bot.send_message(message.chat.id, "Выбери что хочешь сделать?: ",reply_markup=income_keyboard)
    bot.register_next_step_handler(message, get_info, number, data)


def get_info(message, number, data):
    if message.text == "Dogs":
        bot.send_message(message.chat.id, data[number][2])

    elif message.text == "Cats":
        bot.send_photo(message.chat.id, data[number][1])

    else:
        bot.send_message(message.chat.id, "До свидания")

bot.polling()