#!/usr/bin/env python
# coding=utf-8
# https://t.me/unk9vvn
# AVI
import telegram, logging
from telegram.ext import *
from telegram import ReplyKeyboardRemove


updater = Updater('Token')
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
    bot.sendContact(chat_id=364525105,
                    disable_notification=True,
                    contact=update.message.contact)

def linker_location(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(chat_id=update.message.chat_id,
                     text="""🗯 با سلام,برای عضویت در کانال های خصوصی میبایست حق عضویت پرداخت کنید مبلغ عضویت #صد هزار تومان میباشد که با استفاده از درگاه تیم میتونید هزینه را پرداخت نمایید,

https://idpay.ir/unk9vvn

🗯 اما در خصوص روند کار کانال ها توضیحاتی میبایست داده شود,کانال ها بر اساس نقشه راه ترسیم شده که در لینک زیر میتوانید نقشه راه را مشاهده نمایید محتوا میگیرد,همچنین با جستجو سرفصل های ذکر شده در نقشه راه همراه کلمه #Blackhat #Training میتوانید زیر مجموع سرفصل های نقشه راه را در سایت Blackhat.com مشاهده کنید,

https://t.me/Unk9vvN/447

✅ بدلیل گسترده بودن مطالب ما در هفته کانال هارا بروز و منابع را گسترش میدهیم,اما نکته قابل اهمیت این است که مطالب به سه صورت گرد آوری میشوند,نخست کانالی برای ابزارهای مورد نیاز و کتاب های گلچین شده در موضوعات مختلف که اگر در خصوص موضوعات جاری منابع فارسی زبان هم باشد گزاشته خواهد شد,دوم بصورت پکیج و دور های تصویری که بصورت گسترده موجود میباشد و هر روز بیشتر میشود,سوم بصورت Refrence میباشد که در کانالی مطالبی که در Blog ها و سایت های معتبر دنیا نشر داده میشه ما Refrence خواهیم داد تا در بدست آورد اطلاعات مخاطبان کاملتر تحقیق کنند,
⁉️ اما در خصوص پشتیبانی باید عرض کنم ما یک گروه خصوصی بنام #Unk9_TMW که مخصوص اعضای VIP کانال ها میباشد تشکیل دادیم و همچنین یک گروه صوتی در برنامه #Discord که زیر لینک دانلود برنامه گزاشته شده است داریم که در آنجا هم افراد میتوانند از ساعت 17 الی 22 از افرادی که در کانال صوتی برنامه #Discord مشغول کار هستند کمک و سوالات خود را مطرح کنند البته ما بصورت هفتگی در شب های سه شنبه و جمعه از ساعت 22 الی 2 بامداد جلسه جمعی هم خواهیم داشت که میتوانید از این جلسات هم استفاده کنید,

https://discordapp.com/download

⚠️ و نکته آخر قوانین کانال ها به چه صورت میباشد: افراد اگر درخواست پکیج یا کتاب خاصی هستند میتوانند به آیدی رباتی که در #Info کانال های خصوصی گزاشته شده مراجعه و درخواست خودشان را مطرح کنند در صورت امکان انجام خواهد شد,اما در خصوص منابعی که در کانال ها گزاشته شده مبایست این نکته را عرض کنم که #اگر #شخص #تازه #وارد #منابع را برای افرادی که در کانال ها عضو نیستند ارسال کند شخص از کانال ها حذف خواهد شد,البته ارسال به #Saved #as #Messages تلگرام موردی نخواهد داشت و #Seen پست هارا بالا نخواهد برد اما ارسال به افراد غیر مجاز موجب بالا رفتن #Seen پست ها شده و فرد جدید شناسایی و حذف خواهد شد,
⚠️ برای #عضویت در کانال ها,بعد از پرداخت مبلغ عضویت یک #عکس #از #آبربانک خود به گونه ای که فقط شماره کارت و اسم فامیل شما دیده شود برای ربات ارسال کنید و منتظر باشید تا لینک ها ارسال شود,ادمین ربات هر #چهار ساعت ربات را چک میکند, #نکته: علت درخواست عکس آبربانک این است که افراد سودجو با استفاده از اطلاعات حساب های دزدی در درگاه ما پرداخت انجام ندهند,
این کانال ها فقط و فقط برای افرادی که مانند ما علاقمند به کسب دانش روز و حرفه ای هستند تشکیل شده,با تشکر @Unk9vvN""", reply_markup=ReplyKeyboardRemove())
    bot.sendLocation(chat_id=364525105,
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
