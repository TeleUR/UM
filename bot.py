#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import time
import json
import sys
from telebot import types
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")
#redis = r.StrictRedis(host='localhost', port=6379, db=0)
token = '295551995:AAHQzY0szoesnJyD71MrUWUtn-NJDqIK4s4' # Your Token Here
bot = telebot.TeleBot(token)
admin = 242361127
bot.send_message(admin,'Bot Started')

#Start Project!

@bot.message_handler(commands=['start'])
def start(m):
  #redis.sadd('users','{}'.format(m.from_user.id))
  markup = types.ReplyKeyboardMarkup()
  echo = types.KeyboardButton('echo')
  umbrella = types.KeyboardButton('CyberT')
  robots = types.KeyboardButton('RoBots')
  Personnels = types.KeyboardButton('Personnels')
  Web = types.KeyboardButton('Web Services')
  Support = types.KeyboardButton('About us')
  Jobs = types.KeyboardButton('Jobs')
  Order = types.KeyboardButton('Order')
  markup.add(echo)
  markup.add(umbrella,Personnels)
  markup.add(robots,Web)
  markup.add(Order,Jobs,Support)
  bot.send_message(m.chat.id,'''
*Welcome to CyberT BOT ...*

This robot is for Provide Description, Help, Support, Presentation for Products and Services and more...
------------------
		سلام😂
''',reply_markup=markup,parse_mode='markdown')

####################

@bot.message_handler(regexp='^CyberT')
def um(m):
   bot.send_message(m.chat.id,'''
*CYB3RT bot...*

This is a copy from Umbrella bot.

*☂Products & Services:*
     API Web Services
     Online Web Tools
     Web Masters Plugins
     Telegram Robots
     Computer Programs
     Mobile Applications
     Website Design
     Scripting
     and more...

_🌂khkhkhkh_
''',parse_mode='markdown')

####################

@bot.message_handler(regexp='^Personnels')
def te(m):
 try:
   mer = types.ReplyKeyboardMarkup()
   bac = types.KeyboardButton('Back')
   sh = types.KeyboardButton('4li 😉 ')
   Ya = types.KeyboardButton('Javad')
   mr = types.KeyboardButton('Komeil ')
   en = types.KeyboardButton('Reza')
   ab = types.KeyboardButton('Dr. Abdol Hussein Efatnezhad Mohebi')
   ra = types.KeyboardButton('Mr Radman Hayati')
   ni = types.KeyboardButton('Mr Nima Tabesh')
   sa = types.KeyboardButton('Mrs. Sahar Rad')
   amin = types.KeyboardButton('Mr Amin Kavari Nasab')
   na = types.KeyboardButton('Mrs. Nadiya Alizade')
   mer.add(bac)
   mer.add(sh)
   mer.add(Ya)
   mer.add(mr)
   mer.add(en)
 #  mer.add(ab)
 #  mer.add(ra)
  # mer.add(ni)
  # mer.add(sa)
   #mer.add(amin)
  # mer.add(na)
   bot.send_message(m.chat.id,'''
*Umbrella Team Personnels:*
`select a personnels for see biograpy...`
''',parse_mode='markdown',reply_markup=mer)
 except:
   print 'Error'
####################

@bot.message_handler(regexp='^About us')
def sup(m):
 try:
  markup = types.InlineKeyboardMarkup()
  wep = types.InlineKeyboardButton('Website',url='https://telegram.me/cliali')
  gp = types.InlineKeyboardButton('Master Group',url='https://telegram.me/cliali')
  ch = types.InlineKeyboardButton('Master Channel',url='https://telegram.me/cliali')
  mr = types.InlineKeyboardButton('Master RoBot',url='https://telegram.me/cliali')
  po = types.InlineKeyboardButton('Instagram',url='https://telegram.me/cliali')
  admin = types.InlineKeyboardButton('Master Admin',url='https://telegram.me/cliali')
  markup.add(wep,gp)
  markup.add(ch,mr)
  markup.add(po,admin)
  bot.send_message(m.chat.id,'''
Umbrella Team Logs:
  Team Personnels: 12
  Robots Admins: 7
  Robots Groups: 507
  All Robots Users: 42588
  Channel Members: 1664
  All of Robots: 11
  All of Web Services: 7

Umbrella Team Contacs:
  Website: None :D
  E-Mail: None :D
  Master Channel: None @CyberHelp , @Cyb3rHelp
  Master Robot: @CyberTrobot
  Instagram: UmbrellaTeam
  Admin: @CliAli
  Number: +98933*******
  Bot Version: 2.0

Umbrella Projects Team
Iranian Best & International
''',reply_markup=markup)
 except:
  print 'Error'

#####################

@bot.message_handler(regexp='^4li 😉')
def mosy(m):
  bot.send_message(m.chat.id,'Developer And Admin Of The Bot!')

#####################

@bot.message_handler(regexp='^Komeil')
def mosy(m):
  bot.send_message(m.chat.id,'Admin And Manager')

#####################

@bot.message_handler(regexp='^Javad')
def mosy(m):
  bot.send_message(m.chat.id,'Developer And Admin Of The Bot!')

#####################

@bot.message_handler(regexp='^Reza')
def mosy(m):
  bot.send_message(m.chat.id,'Admin And Manager')

######################

@bot.message_handler(regexp='^Jobs')
def job(m):
 try:
  markup = types.InlineKeyboardMarkup()
  job = types.InlineKeyboardButton('Job Singup Form',url='https://telegram.me/cliali')
  markup.add(job)
  bot.send_message(m.chat.id,'''
If you want join to Umbrella Team, signup and send Job Form
''',reply_markup=markup)
 except:
   print 'Error'

#####################

@bot.message_handler(regexp='^Back')
def back(m):
 try:
  markup = types.ReplyKeyboardMarkup()
  echo = types.KyboardButton('echo')
  umbrella = types.KeyboardButton('CyberT')
  robots = types.KeyboardButton('RoBots')
  Personnels = types.KeyboardButton('Personnels')
  Web = types.KeyboardButton('Web Services')
  Support = types.KeyboardButton('About us')
  Jobs = types.KeyboardButton('Jobs')
  Order = types.KeyboardButton('Order')
  markup.add(echo)
  markup.add(umbrella,Personnels)
  markup.add(robots,Web)
  markup.add(Order,Jobs,Support)
  bot.send_message(m.chat.id,'*Main Menu:*',reply_markup=markup,parse_mode='markdown')
 except:
  print 'Error'

####################

@bot.message_handler(regexp='^RoBots')
def baeck(m):
  markup = types.ReplyKeyboardMarkup()
  back = types.KeyboardButton('Back')
  bc = types.KeyboardButton('Cyb3rTrobot')
  asl = types.KeyboardButton('Asl RoBot')
  markup.add(back)
  markup.add(bc)
  markup.add(asl)
  bot.send_message(m.chat.id,'Select a *RoBot:*',parse_mode='markdown',reply_markup=markup)
####################

@bot.message_handler(regexp='^Order')
def order(m):
  markup = types.InlineKeyboardMarkup()
  ui = types.InlineKeyboardButton('Private',url='https://telegram.me/CliAli')
  op = types.InlineKeyboardButton('Bot',url='https://telegram.me/CyberTrobot')
  markup.add(ui)
  markup.add(op)
  bot.send_message(m.chat.id,'Our Bot And Owner Private',reply_markup=markup)

#####################

@bot.message_handler(regexp='^Web Services')
def web(m):
  markup = types.ReplyKeyboardMarkup()
  back = types.KeyboardButton('Back')
 # key = types.KeyboardButton('Your TexT Here')
  markup.add(back)
 # markup.add(key)
  bot.send_message(m.chat.id,'Select a Web Service:',reply_markup=markup,parse_mode='markdown')

#####################

@bot.message_handler(regexp='^Cyb3rTrobot')
def bck(m):
  bot.send_message(m.chat.id,'''
*Description:* In this robot you can Make QR Code and Barcode Easy Handeling and Read QR Codes by File or Camera and you can Hashed and Unhashed Strings...

*Making Date:* 19-06-2016

*Username:* [@Cyn3rTrobot](https://telegram.me/Cyb3rTrobot)

Programmer: [ 4li ](https://telegram.me/Cliali)

*Desinger:* Mrs. Leyla Ahmadi 😍😂

*Adviser:* Parsa Daneshvar
''',parse_mode='markdown',disable_web_page_preview=True)

####################

@bot.message_handler(regexp='^Asl RoBot')
def bck(m):
  bot.send_message(m.chat.id,'''
*Description:* In this robot you can Save Your Information Like Phone Number & Channel and...

*Making Date:* 19-06-2016

*Username:* [No :D](https://telegram.me/Cyb3rTrobot)

Programmer: [ 4li ](https://telegram.me/Mosydev)

*Desinger:* Mrs. Leyla Ahmadi 😍😂

*Adviser:* Parsa Daneshvar
''',parse_mode='markdown',disable_web_page_preview=True)

###################

@bot.inline_handler(lambda query: query.query == query.query)
def query_text(query):
 if query.from_user.id == 242361127 or query.from_user.id == 242361127:
   id = query.from_user.id
   user = query.from_user.username
   name = query.from_user.first_name
   test = types.InlineQueryResultArticle('1', 'Admin', types.InputTextMessageContent('Your Are A *Admin*\nYour Name: {}\nYour Rank: *Admin*'.format(name),parse_mode='Markdown'),thumb_url='http://yon.ir/kXyZ')
   bot.answer_inline_query(query.id, [test], cache_time="10")
 else:
   err = types.InlineQueryResultArticle('1', 'Member', types.InputTextMessageContent('''
*Umbrella Copy Project Team*

This user is `Normal` Member
''',parse_mode='Markdown'),thumb_url='http://yon.ir/kXyZ')
   bot.answer_inline_query(query.id, [err], cache_time="10")

#####################
@bot.message_handler(regexp='^echo')
def echo0(m):
    bot.send_message(m.chat.id, '''
/echo *TEXT*
برای بولد کردن متن

/echo _TEXT_
برای ایتالیک کردن متن
 
/echo `TEXT`
برای نوشتن کد مانند

/echo [اسم روی هایپر)[لینک هایپر)

/echo TEXT
تکرار متن شما

😂😂😂

تسته ها!!!
''' , parse_mode='HTML',disable_web_page_preview=True)

@bot.message_handler(commands=['echo'])
def echo(m):
    bot.send_message(m.chat.id,  m.text.replace('/echo', ''), parse_mode='Markdown')


#End Project!

bot.polling(True)
