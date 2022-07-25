import telebot
import sqlite3


bot = telebot.TeleBot('5363558423:AAEEKqNz2eiBmB0B_8bXWynyvtwmxcVzAhI') 

conn = sqlite3.connect('C:/VSprojects/valera/hochu/db.sqlite3') 
cursor = conn.cursor()

cursor.execute('SELECT *, max(id) FROM home_frm1 WHERE sent = False')
imya = cursor.fetchone()
a = str(imya[1])
b = str(imya[2])
c = str(imya[3])
bot.send_message(chat_id='1171882715', text=a+'\n'+c)

cursor.execute('UPDATE home_frm1 SET sent == ? WHERE sent == ?', ('1','0'))
conn.commit()

conn.close()

'''Никита 1171882715'''
'''Валера 335235105'''