
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
    usermarkup.row('Picnic', 'Rafaello')
    usermarkup.row('Alpen Gold Funduk', 'Dark')
    usermarkup.row('Alpen Gold', 'KitKat')
    usermarkup.row('заказ')
    bot.send_message(message.from_user.id, "You're welcome", reply_markup=usermarkup)

#Ответы на вопросы и сказочки)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Picnic' or message.text == 'пикник':
        bot.send_message(message.chat.id, assortiment.picnic)
        answer = assortiment.picnic
        log(message, answer)
    elif message.text == 'Rafaello' or message.text == 'рафаелло':
        bot.send_message(message.chat.id, assortiment.rafaello)
        answer = assortiment.rafaello
        log(message, answer)
    elif message.text == 'Alpen Gold Funduk':
        bot.send_message(message.chat.id, assortiment.apgfd)
        answer = assortiment.apgfd
        log(message, answer)
    elif message.text == 'Dark':
        bot.send_message(message.chat.id, assortiment.dark)
        answer = assortiment.dark
        log(message, answer)
    elif message.text == 'Alpen Gold':
        bot.send_message(message.chat.id, assortiment.apgd)
        answer = assortiment.apgd
        log(message, answer)
    elif message.text == 'KitKat':
        bot.send_message(message.chat.id, assortiment.kitkat)
        answer = assortiment.kitkat
        log(message, answer)
    elif message.text == 'заказ':
        bot.send_message(message.chat.id, 'Мы свяжемся с Вами в кратчайшие сроки')
        zakazchik = ('id = ' + str(message.from_user.id) + '\nИмя: ' + str(message.from_user.first_name))
        time.sleep(15)
        bot.send_message(config.pasha, 'Новый заказ!\n' + str(zakazchik))
        answer = 'Мы свяжемся с Вами в кратчайшие сроки для уточнения заказа'
        log(message,answer)
    else:
        bot.send_message (message.chat.id, 'Я Вас не понимаю, извините')
        answer = 'Я Вас не понимаю, извините'
        log(message, answer)

bot.polling(none_stop=True, interval=0)


