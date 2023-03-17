import telebot
from my_token import token
from parsing import get_post

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    data = get_post()

    bot.send_message(message.chat.id,"Привет!!Добро пожаловать в Кайнар!")
    
    if len(data) == 1:
        bot.send_message(message.chat.id,"У нас появился новый дружок!")


def get_info(message, number, data):
    if message.text == "Description":
        bot.send_message(message.chat.id, data[number][2])

    elif message.text == "Photo":
        bot.send_photo(message.chat.id, data[number][1])

    else:
        bot.send_message(message.chat.id, "До свидания")


bot.polling()