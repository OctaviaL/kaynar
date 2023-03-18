import telebot
from my_token import token
from parsing import main

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    post = main()

    bot.send_message(message.chat.id,"Привет!!Добро пожаловать в Кайнар!")
    
    if len(post) == 0:
        bot.send_message(message.chat.id,"У нас пока нет новых друзей!!")

    c = 0
    for i in post:
        c += 1
        bot.send_message(message.chat.id, str(c) + '. ' + i[0]) 

def get_info(message, post):
    if message.text == "Что нового?":
        bot.send_message(message.chat.id, post)
    else:
        bot.send_message(message.chat.id, "Посетите наших друзей!")


bot.polling()