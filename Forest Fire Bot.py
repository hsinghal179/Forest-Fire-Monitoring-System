#!/usr/bin/env python
# coding: utf-8

# In[1]:


from telegram import *
from telegram.ext import *
import csv
import urllib.request
import os


# In[ ]:


while(True):
    token = "Telegram Bot Token"
    bot = Bot(token)
    updater = Updater(token,use_context=True)
    dispatcher = updater.dispatcher

    # Start Command
    data1 = "Welcome to the Bot\nType '/test' to test the bot \nType '/fire' to check the status of forest fire"
    def start_fun(update:Update,context:CallbackContext):
        bot.send_message(chat_id=update.effective_chat.id, text=data1)

    start_value = CommandHandler("start",start_fun)
    dispatcher.add_handler(start_value)

    # Test Command
    data2 = "This project is completely developed by Team 21E279280-SRM_University"
    def test_fun(update:Update,context:CallbackContext):
        bot.send_message(chat_id=update.effective_chat.id, text=data2)

    test_value = CommandHandler("test",test_fun)
    dispatcher.add_handler(test_value)

    #Fetch Data from thinkspeak
    def fetch():
        url = 'https://thingspeak.com/channels/"ChannelValue"/field/1.csv'
        urllib.request.urlretrieve(url, '/Users/Harshit/1.csv')
        with open('/Users/Harshit/1.csv') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                msg=row[2]
        os.remove('/Users/Harshit/1.csv')
        return str(msg)


    # Fire Command
    data3 = fetch()
    if int(data3) > 900:
        data3 = "Fire Alert at Phase-1"
    else:
        data3 = "No risk of fire at any Phase"
    def fire_fun(update:Update,context:CallbackContext):
        bot.send_message(chat_id=update.effective_chat.id, text=data3)

    fire_value = CommandHandler("fire",fire_fun)
    dispatcher.add_handler(fire_value)

    #Starter
    updater.start_polling()

