import telebot

bot = telebot.TeleBot('5363558423:AAEEKqNz2eiBmB0B_8bXWynyvtwmxcVzAhI')

@bot.message_handler(commands=['start'])
def send(message):
   x = str(message.chat.id)
   bot.send_message(message.chat.id, text = x)
   
bot.polling()