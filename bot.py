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
    item1 = types.KeyboardButton("π€· 2 Photos - The same man ?")
    item2 = types.KeyboardButton("π What emotions ?")
    item3 = types.KeyboardButton("π§ Music !")
    item4 = types.KeyboardButton("π¨βπ©βπ¦ How many people in the photo ?")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,
                     'Hello, {0.first_name} π, \n'
                     '\n'
                     'I am a brand-new telegramm bot.\n'
                     'I can do a lot with your photos πͺ.\n'
                     'Tap on any button to see my features. Check it out ! π'.format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "π€· 2 Photos - The same man ?":
            print("Π― Π² ΠΏΠ΅ΡΠ²ΠΎΠΌ ΠΌΠ΅Π½Ρ")
            work1[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("βͺ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Cool, You need to upload two photos to find out,'
                             ' if the people in them are the same ! π'.format(
                                 message.from_user), reply_markup=markup)
            while work1[0] == 1:
                print("Π― Π² ΡΠΈΠΊΠ»Π΅")
                if len(data) == 2:
                    if compare(data[0], data[1]) == 1:
                        print(data[0], data[1])
                        bot.send_message(message.chat.id, "ΠΠ° ΡΠΎΡΠΎΠ³ΡΠ°ΡΠΈΡΡ ΠΎΠ΄ΠΈΠ½ ΠΈ ΡΠΎΡ ΠΆΠ΅ ΡΠ΅Π»ΠΎΠ²Π΅ΠΊ ! π₯³")
                    else:
                        bot.send_message(message.chat.id, "ΠΠ° ΡΠΎΡΠΎΠ³ΡΠ°ΡΠΈΡΡ ΡΠ°Π·Π½ΡΠ΅ Π»ΡΠ΄ΠΈ ! π€·")
                    os.remove(data[1])
                    os.remove(data[0])
                    data.clear()
                if work1[0] == 0:
                    break



        elif message.text == "π Analyze":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            work3[0] = 1
            item1 = types.KeyboardButton("βͺ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'So, give me your picture to get some interesting information on your photo...'.format(
                                 message.from_user), reply_markup=markup)
            while work3[0] == 1:
                bot.send_message(message.chat.id, "Here is your information:")
                os.remove(data[0])
                data.clear()


        elif message.text == "π¨βπ©βπ¦ How many people in the photo ?":
            print("Π― Π² Π»ΡΠ΄ΡΡ")
            work2[0] = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("βͺ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'You can easily define how many people are in a photo,'
                             ' just upload it here! π'.format(
                                 message.from_user), reply_markup=markup)
            while work2[0] == 1:
                if len(data) == 1:
                    time.sleep(3)
                    face_rec(data[0])
                    bot.send_photo(message.chat.id, open('images/new.jpg', 'rb'))
                    bot.send_message(message.chat.id, f"ΠΠ° ΠΊΠ°ΡΡΠΈΠ½ΠΊΠ΅ ΠΎΠ±Π½Π°ΡΡΠΆΠ΅Π½ΠΎ {face_rec(data[0])} ΡΠ΅Π»ΠΎΠ²Π΅ΠΊ(Π°) !")
                    os.remove(data[0])
                    data.clear()
                if work2[0] == 0:
                    break



        elif message.text == "π§ Music !":
            print("Π― Π² ΠΌΡΠ·ΡΠΊΠ΅")
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("βͺ Back")
            markup.add(item1)
            bot.send_message(message.chat.id,
                             'Wow, just take a picture and send it here. '
                             'I will suggest you a music playlist for your mood! π'.format(
                                 message.from_user), reply_markup=markup)
        elif message.text == "βͺ Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            print("Π― Π²ΡΡΠ΅Π»")
            item1 = types.KeyboardButton("π€· 2 Photos - The same man ?")
            item2 = types.KeyboardButton("π Analyze")
            item3 = types.KeyboardButton("π§ Music !")
            item4 = types.KeyboardButton("π¨βπ©βπ¦ How many people in the photo ?")

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id,
                             "OK, let's pick something else...".format(
                                 message.from_user), reply_markup=markup)

            work1[0] = 0
            work2[0] = 0
            work3[0] = 0



bot.polling(none_stop=True)