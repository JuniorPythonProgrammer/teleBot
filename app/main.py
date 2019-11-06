# -*- coding: utf-8 -*-
import telebot
import constant
import random
import game


bot = telebot.TeleBot(constant.token)

global joke_number, game1
joke_number = 0
game1 = False

@bot.message_handler(commands=['start'])
def start_keyboard(message):
    initial_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    initial_keyboard.row('/start','/stop')
    initial_keyboard.row(constant.messages_keys['greeting'][2], constant.messages_keys['joke'])
    initial_keyboard.row(constant.messages_keys['random_coin'], constant.messages_keys['game'])
    bot.send_message(message.from_user.id, constant.messages_reply['greeting'], reply_markup=initial_keyboard)

@bot.message_handler(commands=['stop'])
def stop_keyboard(message):
    hide_keybord = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '👀', reply_markup=hide_keybord)

@bot.message_handler(content_types=["text"])
def conversation(message):
    global joke_number, game1
    if constant.messages_keys['game'] in message.text:
        game1 = True
    if game1 == False:
        for greeting in constant.messages_keys['greeting']:
            if greeting in message.text:
                bot.send_message(message.chat.id, constant.messages_reply['greeting'][0])
        if constant.messages_keys['joke'] in message.text:
            bot.send_message(message.chat.id, constant.messages_reply_joke[joke_number])
            if joke_number == len(constant.messages_reply_joke)-1:
                joke_number = 0
            else:
                joke_number += 1
        elif constant.messages_keys['random_coin'] in message.text:
            bot.send_message(message.chat.id, random.choice(constant.messages_reply['random_coin']))
        else:
            if message.text != constant.messages_keys['greeting'][2]:
                bot.send_message(message.chat.id, constant.messages_reply['error'])
    elif game1 == True:
        game.game_sapper(message.chat.id, message.text)
    if game.gg == True:
        game1 = False
        game.gg = False
        


if __name__ == '__main__':
    bot.polling(none_stop=True)