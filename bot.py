
import telebot
import config
import assortiment
import time

bot = telebot.TeleBot(config.token)
chid = (config.chat_id)


upd = bot.get_updates()
#print(upd)

"""last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)
"""

print(bot.get_me())

def log(message, answer):
    print("\n ------")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}, (id = {2}) \nText: {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print("Answer: " + answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    usermarkup = telebot.types.ReplyKeyboardMarkup(True, False)
    usermarkup.row('/start')
    usermarkup.row('picnic', 'snickers')
    usermarkup.row('Tofee', 'bounty')
    usermarkup.row('заказ')
    bot.send_message(message.from_user.id, "You're welcome", reply_markup=usermarkup)

#Ответы на вопросы и сказочки)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'picnic' or message.text == 'пикник':
        bot.send_message(message.chat.id, assortiment.picnic)
        answer = assortiment.picnic
        log(message, answer)
    elif message.text == 'snickers' or message.text == 'сникерс':
        bot.send_message(message.chat.id, assortiment.snickers)
        answer = assortiment.snickers
        log(message, answer)
    elif message.text == 'bounty':
        bot.send_message(message.chat.id, assortiment.bounty)
        answer = assortiment.bounty
        log(message, answer)
    elif message.text == 'Tofee':
        bot.send_message(message.chat.id, assortiment.tofee)
        answer = assortiment.tofee
        log(message, answer)
    elif message.text == 'заказ':
        bot.send_message(message.chat.id, 'Мы свяжемся с Вами в кратчайшие сроки')
        zakazchik = ('id = ' + str(message.from_user.id) + '\nИмя: ' + str(message.from_user.first_name))
        time.sleep(15)
        bot.send_message(config.chat_id, 'Новый заказ!\n' + str(zakazchik) + ' ' + str(message.text))
        answer = 'Мы свяжемся с Вами в кратчайшие сроки'
        log(message,answer)
    else:
        bot.send_message (message.chat.id, 'Я Вас не понимаю, извините')
        answer = 'Я Вас не понимаю, извините'
        log(message, answer)

bot.polling(none_stop=True, interval=0)


