import telebot
import constant
from main import bot
import main
import random



global complexity, complexity_beginning, complexity_end, mines_namber, geme_over, butt, buttons, butt1, gg, uniqueness
complexity = 0
complexity_beginning = False
complexity_end = False
geme_over = False
mines_namber = []
butt = False
butt1 = True
buttons = []
gg = False
uniqueness = True


def stop_game(chat_id):
    global complexity, complexity_beginning, complexity_end, mines_namber, geme_over, butt, buttons, butt1, game1, gg
    initial_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    initial_keyboard.row('/start','/stop')
    initial_keyboard.row(constant.messages_keys['greeting'][2], constant.messages_keys['joke'])
    initial_keyboard.row(constant.messages_keys['random_coin'], constant.messages_keys['game'])
    bot.send_message(chat_id, constant.messages_reply['greeting'][1], reply_markup=initial_keyboard)
    gg = True
    complexity = 0
    complexity_beginning = False
    complexity_end = False
    geme_over = False
    mines_namber = []
    butt = False
    butt1 = True
    buttons = []


def game_sapper(chat_id, message_text):
   
    global complexity, complexity_beginning, complexity_end, mines_namber, geme_over, butt, buttons, butt1, game1, gg, uniqueness
    
    if message_text == 'стоп игра':
        stop_game(chat_id)

    elif complexity_beginning == False:
        bot.send_message(chat_id, constant.messages_game_sapper['description'][0])
        game1_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
        game1_keyboard.row(constant.messages_game_sapper['complexity'][0])
        game1_keyboard.row(constant.messages_game_sapper['complexity'][1])
        game1_keyboard.row(constant.messages_game_sapper['complexity'][2])
        game1_keyboard.row(constant.messages_game_sapper['complexity'][3])
        game1_keyboard.row(constant.messages_game_sapper['complexity'][4])
        bot.send_message(chat_id, constant.messages_game_sapper['description'][1], reply_markup=game1_keyboard)
        complexity_beginning = True
    
    elif complexity_beginning == True and complexity_end == False:
        complexity_end = True
        if message_text == constant.messages_game_sapper['complexity'][0]:
            complexity = 5
        elif message_text == constant.messages_game_sapper['complexity'][1]:
            complexity = 10
        elif message_text == constant.messages_game_sapper['complexity'][2]:
            complexity = 15
        elif message_text == constant.messages_game_sapper['complexity'][3]:
            complexity = 20
        elif message_text == constant.messages_game_sapper['complexity'][4]:
            complexity = 24
        else:
            bot.send_message(chat_id, constant.messages_game_sapper['error'][0])
            complexity_end = False
        if complexity > 0:
            mines = 0
            while mines<complexity:
                namber = random.randrange(1, 26)
                namb = False
                for nam in mines_namber:
                    if nam == namber:
                        namb = True
                if namb == False:
                    mines_namber.append(namber)
                    mines += 1
        if complexity_end == True:
            game2_keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
            game2_keyboard.row('1','2','3','4','5')
            game2_keyboard.row('6','7','8','9','10')
            game2_keyboard.row('11','12','13','14','15')
            game2_keyboard.row('16','17','18','19','20')
            game2_keyboard.row('21','22','23','24','25')
            game2_keyboard.row('стоп игра')
            bot.send_message(chat_id, constant.messages_game_sapper['description'][2], reply_markup=game2_keyboard)
        print(sorted(mines_namber))
        print(len(mines_namber))

    elif complexity_beginning == True and complexity_end == True and geme_over == False:
        for num in range(26):
            if str(num) == message_text:
                butt1 = False
        if butt1 == True:
            bot.send_message(chat_id, constant.messages_game_sapper['error'][1])
        if butt1 == False:
            for but in buttons:
                if but == message_text:
                    bot.send_message(chat_id, constant.messages_game_sapper['error'][2])
                    butt = True
        if message_text == 'стоп игра':
            stop_game(chat_id)
            butt = True
        if butt == False:
            for boom in mines_namber:
                if boom == int(message_text):
                    bot.send_message(chat_id, constant.messages_game_sapper['wrond'][0])
                    bot.send_message(chat_id, constant.messages_game_sapper['wrond'][1])
                    stop_game(chat_id)
                    geme_over = True
            if geme_over == False:
                bot.send_message(chat_id, constant.messages_game_sapper['right'][0])
                buttons.append(message_text)
                if len(buttons) == 1 and complexity == 24:
                    bot.send_message(chat_id, constant.messages_game_sapper['right'][6])
                    stop_game(chat_id)
                if len(buttons) == 3:
                    bot.send_message(chat_id, constant.messages_game_sapper['right'][1])
                elif len(buttons) == 5:
                    if complexity == 5 or complexity == 10 or complexity == 15:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][2])
                    elif complexity == 20:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][5])
                        stop_game(chat_id)
                elif len(buttons) == 10:
                    if complexity == 5 or complexity == 10:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][3])
                    elif complexity == 15:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][5])
                        stop_game(chat_id)
                elif len(buttons) == 15:
                    if complexity == 5:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][4])
                    elif complexity ==10:
                        bot.send_message(chat_id, constant.messages_game_sapper['right'][5])
                        stop_game(chat_id)
                elif len(buttons) == 20:
                    bot.send_message(chat_id, constant.messages_game_sapper['right'][5])
                    stop_game(chat_id)
        butt = False
        butt1 = True
        geme_over = False