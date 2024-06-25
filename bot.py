from func import *
import telebot

TOKEN = '7076757635:AAFp8PmQVz6ddsmUl2ZpQzYZ7CSDKCObakI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Отправь название города на английском и я покажу, сколько там градусов')

@bot.message_handler(content_types=['text'])
def send_temp(message):
    location = message.text.lower()
    bot.send_message(message.chat.id, get_temperature(location))



bot.infinity_polling()