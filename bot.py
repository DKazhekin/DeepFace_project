import os
import time

import telebot
from telebot import types

from main import compare
from main import face_rec

TOKEN = '5572151397:AAEFpb0Zw_q118Et5mJgdWFdUtLI84ths4c'

bot = telebot.TeleBot(TOKEN)

data = []

work1 = [1]
work2 = [1]
work3 = [1]

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'images/' + file_info.file_path.split('/')[-1]
    data.append(src)
    print(data)
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🤷 2 Photos - The same man ?")
    item2 = types.KeyboardButton("😐 What emotions ?")
    item3 = types.KeyboardButton("🎧 Music !")
    item4 = types.KeyboardButton("👨‍👩‍👦 How many people in the photo ?")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     'Hello, {0.first_name} 👋, \n'
                     '\n'
                     'I am a brand-new telegramm bot.\n'
                     'I can do a lot with your photos 🪄.\n'
                     'Tap on any button to see my features. Check it out ! 😇'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "🤷 2 Photos - The same man ?":
            print("Я в первом меню")
            work1[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Cool, You need to upload two photos to find out,'
                             ' if the people in them are the same ! 😊'.format(
                                 message.from_user), reply_markup=markup)
            while work1[0] == 1:
                print("Я в цикле")
                if len(data) == 2:
                    if compare(data[0], data[1]) == 1:
                        print(data[0], data[1])
                        bot.send_message(message.chat.id, "На фотографиях один и тот же человек ! 🥳")
                    else:
                        bot.send_message(message.chat.id, "На фотографиях разные люди ! 🤷")
                    os.remove(data[1])
                    os.remove(data[0])
                    data.clear()
                if work1[0] == 0:
                    break



        elif message.text == "😐 Analyze":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            work3[0] = 1
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'So, give me your picture to get some interesting information on your photo...'.format(
                                 message.from_user), reply_markup=markup)
            while work3[0] == 1:
                bot.send_message(message.chat.id, "Here is your information:")
                os.remove(data[0])
                data.clear()


        elif message.text == "👨‍👩‍👦 How many people in the photo ?":
            print("Я в людях")
            work2[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'You can easily define how many people are in a photo,'
                             ' just upload it here! 😜'.format(
                                 message.from_user), reply_markup=markup)
            while work2[0] == 1:
                if len(data) == 1:
                    time.sleep(3)
                    face_rec(data[0])
                    bot.send_photo(message.chat.id, open('images/new.jpg', 'rb'))
                    bot.send_message(message.chat.id, f"На картинке обнаружено {face_rec(data[0])} человек(а) !")
                    os.remove(data[0])
                    data.clear()
                if work2[0] == 0:
                    break



        elif message.text == "🎧 Music !":
            print("Я в музыке")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Wow, just take a picture and send it here. '
                             'I will suggest you a music playlist for your mood! 😌'.format(
                                 message.from_user), reply_markup=markup)
        elif message.text == "⏪ Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            print("Я вышел")
            item1 = types.KeyboardButton("🤷 2 Photos - The same man ?")
            item2 = types.KeyboardButton("😐 Analyze")
            item3 = types.KeyboardButton("🎧 Music !")
            item4 = types.KeyboardButton("👨‍👩‍👦 How many people in the photo ?")

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id,
                             "OK, let's pick something else...".format(
                                 message.from_user), reply_markup=markup)

            work1[0] = 0
            work2[0] = 0
            work3[0] = 0



bot.polling(none_stop=True)