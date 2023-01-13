import os
import time

import telebot
from telebot import types

from main import compare
from main import face_rec
from main import filter_my1
from main import filter_my2
from main import filter_my3

TOKEN = '5572151397:AAEFpb0Zw_q118Et5mJgdWFdUtLI84ths4c'

bot = telebot.TeleBot(TOKEN)

data = []

work1 = [1]
work2 = [1]
work3 = [1]
work4 = [1]
work5 = [1]
work6 = [1]


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
    item3 = types.KeyboardButton("🎨 PhotoFilter")
    item4 = types.KeyboardButton("👨‍👩‍👦 How many people in the photo ?")

    markup.add(item1, item3, item4)

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
                        bot.send_message(message.chat.id, "The photos show the same person ! 🥳")
                    else:
                        bot.send_message(message.chat.id, "There are different people in the photos ! 🤷")
                    os.remove(data[1])
                    os.remove(data[0])
                    data.clear()
                if work1[0] == 0:
                    break



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
                    bot.send_message(message.chat.id, f"There are {face_rec(data[0])} people found in the picture! !")
                    os.remove(data[0])
                    data.clear()
                if work2[0] == 0:
                    break


        elif message.text == "🎨 PhotoFilter":
            print("Запущен редактор фото")

            markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Sketch_multi")
            item2 = types.KeyboardButton("Art")
            item3 = types.KeyboardButton("Arcane_multi")
            item4 = types.KeyboardButton("⏪ Back")
            markup1.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id,
                             'Choose the processing style! 🥳'.format(
                                 message.from_user), reply_markup=markup1)


        elif message.text == "Sketch_multi":
            work4[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Wow, just take a picture and send it here. '
                             'The function turns the photo into an animated view'.format(
                                 message.from_user), reply_markup=markup)
            while work4[0] == 1:
                if len(data) == 1:
                    time.sleep(3)
                    print('1')
                    bot.send_message(message.chat.id, "Wait about a minute, you will see the result soon! 🥳")
                    print(data[0])
                    output = filter_my1(data[0])
                    bot.send_photo(message.chat.id, open(output, 'rb'))
                    os.remove(data[0])
                    data.clear()
                if work4[0] == 0:
                    break

        elif message.text == "Art":
            work5[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Wow, just take a picture and send it here. '
                             'The function turns the photo into an animated view'.format(
                                 message.from_user), reply_markup=markup)
            while work5[0] == 1:
                if len(data) == 1:
                    time.sleep(3)
                    print('1')
                    bot.send_message(message.chat.id, "Wait about a minute, you will see the result soon! 🥳")
                    print(data[0])
                    output = filter_my2(data[0])
                    bot.send_photo(message.chat.id, open(output, 'rb'))
                    os.remove(data[0])
                    data.clear()
                if work5[0] == 0:
                    break

        elif message.text == "Arcane_multi":
            work6[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("⏪ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Wow, just take a picture and send it here. '
                             'The function turns the photo into an animated view'.format(
                                 message.from_user), reply_markup=markup)
            while work6[0] == 1:
                if len(data) == 1:
                    time.sleep(3)
                    print('1')
                    bot.send_message(message.chat.id, "Wait about a minute, you will see the result soon! 🥳")
                    print(data[0])
                    output = filter_my3(data[0])
                    bot.send_photo(message.chat.id, open(output, 'rb'))
                    os.remove(data[0])
                    data.clear()
                if work6[0] == 0:
                    break

        elif message.text == "⏪ Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            print("Я вышел")
            item1 = types.KeyboardButton("🤷 2 Photos - The same man ?")
            item3 = types.KeyboardButton("🎨 PhotoFilter")
            item4 = types.KeyboardButton("👨‍👩‍👦 How many people in the photo ?")

            markup.add(item1, item3, item4)

            bot.send_message(message.chat.id,
                             "OK, let's pick something else...".format(
                                 message.from_user), reply_markup=markup)

            work1[0] = 0
            work2[0] = 0
            work3[0] = 0
            work4[0] = 0


bot.polling(none_stop=True)
