import telebot
import os
token = os.environ["token"]
bot = telebot.TeleBot(token)

bot.send_message('746633302', 'test')
