import random

import telebot
import config

from telebot import types


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Хочу")
    item2=types.KeyboardButton("/help")

    markup.add(item1,item2)

    bot.send_message(message.chat.id, "Привет! Хочешь узнать свежую информацию о МТУСИ? Если хочешь побольше узнать обо мне, напиши: /help".format(message.from_user,bot.get_me()),parse_mode='html',reply_markup=markup)
    sti = open('mem/0T0SkxwWY-c.jpg', 'rb')
    bot.send_photo(message.chat.id, sti)

@bot.message_handler(content_types=['text'])
def kb(message):
    if message.chat.type == 'private':
        if message.text == 'Хочу':
            bot.send_message(message.chat.id,'Отлично! Тогда тебе сюда:https://mtuci.ru/')
        elif message.text=='/help':
            bot.send_message(message.chat.id,'Я пока что знаю только 3 слова: "Привет","Как дела","Пока."Также я могу написать тебе случайное число от 0 до 100 - напиши /random. Если хочешь получить пак снежных оверлеев для монтажа - напиши команду /snow. Если тебе нужно расписание МТУСИ - напиши /sched.')
        elif message.text=='/random':
            bot.send_message(message.chat.id,str(random.randint(0,100)))
        elif message.text=='/sched':
            bot.send_message(message.chat.id,'Отлично! Тогда тебе сюда:https://mtuci.ru/time-table/')
        elif message.text == 'Привет':
            bot.send_message(message.chat.id, 'Ну привет-привет')
        elif message.text=='Как дела':
            bot.send_message(message.chat.id,'У меня всё супер')
        elif message.text=='Пока':
            bot.send_message(message.chat.id,'До скорого')
        elif message.text=='/snow':
            bot.send_message(message.chat.id,'Отлично! Тогда тебе сюда:https://bit.ly/3lTUkZx')
        else:
            bot.send_message(message.chat.id,'Я тебя не понял:(')

# RUN
bot.polling(none_stop=True)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет! Хочешь узнать свежую информацию о МТУСИ?".format(message.from_user,bot.get_me()),parse_mode='html')