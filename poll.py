import telebot
import pyautogui

pyautogui.FAILSAFE = True


bot = telebot.TeleBot("2077081748:AAFau5cRKdlwHYQXIGJwrViIFE9un-AekP8")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)

# class triggers:
#
#     triggers = {}
#
#     def __init__(self):
#         pass
#
#     def check(self, message):
#         for i in range(len(triggers)):
#             if

@bot.message_handler(commands=['sex'])
def send_welcome(message):
	bot.reply_to(message, "うぉおおおお セェエエエエックス うぉおおおお セェエエエエックス   俺はセックスをするんじゃねぇ！俺が！俺自身が！真の！セックスになるんだぁあ！セェエエエックス! やめろ！タケシ！お前これ以上は体力がもたない！ いや！おれはセックスになる！絶対にセックスになるんだ！セェエエエックス! セェエエエックス! やめろ！死んじまうぞタケシ！お前命が尽きても次から(?)セックスができるだろうが！うるせぇ！俺は！死んだってセックスをするんだ！うぉおおお！セェエエエックス")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome to the NUSCAS Halloween Games! \n\n\
NUSCASハロウィン パーティーへようこそ～～　\n \n \
(ゝω´･)～☆")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Here are the list of commands: \n \
    \n /up : walk upwards \n \
    \n /down : walk downwards \n \
    \n /left : walk left \n \
    \n /right : walk right \n \
    \n /restart : restarts the level \n \
    \n /enter: presses enter \n \
    \n /advice : check stage advice")

@bot.message_handler(commands=['w', 'W', 'up'])
def send_welcome(message):
	pyautogui.press('w')

@bot.message_handler(commands=['a', 'A', 'left'])
def send_welcome(message):
	pyautogui.press('a')

@bot.message_handler(commands=['s', 'S', 'down'])
def send_welcome(message):
	pyautogui.press('s')

@bot.message_handler(commands=['d', 'D', 'right'])
def send_welcome(message):
	pyautogui.press('d')

@bot.message_handler(commands=['r', 'R', 'restart'])
def send_welcome(message):
	pyautogui.press('r')

@bot.message_handler(commands=['enter'])
def send_welcome(message):
	pyautogui.press('enter')

@bot.message_handler(commands=['advice'])
def send_welcome(message):
	pyautogui.press('l')


bot.infinity_polling()
