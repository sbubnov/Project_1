from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

import logging
import ephem
import datetime


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO,filename='bot.log')


def greet_user(bot,update):
    text='Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot,update):
    user_text=update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def get_planet(bot,update):
    date = str(datetime.date.today())
    user_text = update.message.text.split()
    planet_name = str(user_text[-1])
    if planet_name == 'Mars':
        planet_date = ephem.Mars(date)
        constellation = ephem.constellation(planet_date)
        update.message.reply_text(constellation)
    elif planet_name == 'Saturn':
        planet_date = ephem.Saturn(date)
        constellation = ephem.constellation(planet_date)
        update.message.reply_text(constellation)
    elif planet_name == 'Jupiter':
        planet_date = ephem.Jupiter(date)
        constellation = ephem.constellation(planet_date)
        update.message.reply_text(constellation)


def main():
    mybot=Updater('754408823:AAFdukXDYkdqin8g3R3WUIgQi9pRCy0ZMmY')
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler('start',greet_user))
    dp.add_handler(CommandHandler('planet',get_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()

