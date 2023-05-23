import time
import telebot
from telebot import types

TOKEN='5886307552:AAH9emfOiJ39mE5sr0rnF66DtihtCkZKPaA'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    bot.send_message(message.chat.id, "Привет! Как твоё здоровье, друг?")


@bot.message_handler(content_types=['text'])
def get_handle_text(message):
    if message.text in ["мне плохо", "я болею", "у меня температура", "болит горло", "болит голова","насморк", "сопли", "слабость", "все уроды", "боль","заболел","болею","болит зуб","болит живот"]:
        bot.send_message(message.chat.id, "Это не хорошо, но поправимо")
        bot.send_message(message.chat.id, "Я вам сейчас попытаюсь помочь! Выберете ведущий симптом, который больше всего вам сейчас неприятен")

        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Температура выше 38,5С")
        btn2 = types.KeyboardButton("Болит горло")
        btn3 = types.KeyboardButton("Болит зуб")
        btn4 = types.KeyboardButton("Болит живот")
        btn5 = types.KeyboardButton("Болит голова")
        btn6 = types.KeyboardButton("Диарея")
        btn7 = types.KeyboardButton("Насморк")
        btn8 = types.KeyboardButton("Тошнит")
        btn9 = types.KeyboardButton("Упал и кажется что-то не так")
        btn10 = types.KeyboardButton("Ничего не вижу")
        btn11 = types.KeyboardButton("Появилась сыпь")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.chat.id, "Прежде чем нажать на кнопку, подумай хорошо", reply_markup=markup)


    elif message.text == "Температура выше 38,5С":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Лучший препарат от температуры - ИБУПРОФЕН, 400 мг, каждые 8 часов", reply_markup=markup)

    elif message.text == "Болит горло":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Полоскание: дедовские методы  -  соль и сода, слабый раствор йода. Теплое питье (очень хорошо молоко и мёд). Препараты: тантум верде, леденцы с анестетиком. При боли в горле и высокой температуре необходима консультация специалиста. Не забудьте стрептотест", reply_markup=markup)
       
    elif message.text == "Болит зуб":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Лучший препарат от боли - ИБУПРОФЕН, 400 мг, каждые 8 часов, полоскание содой или любым антисептиком разрешенным для полоскания ротовой полости. Обязательно обратитесь к врачу в ближайшее время", reply_markup=markup)

    elif message.text == "Болит живот":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Самолечение не допустимо! Обратитесь к врачу незамедлительно!!!", reply_markup=markup)

    elif message.text == "Болит голова":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "ИБУПРОФЕН, 200 мг, Спазмолгон, 1 т и их аналоги. Если имеютя неврологические нарушения (нарушения координации, нарушени речи, глотания, движения и т.д - незамедлительно обратитесь к врачу", reply_markup=markup)

    elif message.text == "Диарея":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Лоперамид согласно инструкции (экстренная помощь) + панкреатин и его аналоги согласно инструкции + пробиоики согласно инструкции", reply_markup=markup)

    elif message.text == "Насморк":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Снуп, Аквамарис, Риностоп и их аналоги. Если аллергического характера, то Авамис или его аналоги согласно инструкции", reply_markup=markup)

    elif message.text == "Тошнит":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Ношпа 2 табл, панкреатин 2 табл. Исскуственно вызванная рвота. Если не помогает - обратиться к врачу. ", reply_markup=markup)

    elif message.text == "Упал и кажется что-то не так":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Самолечение не допустимо! Обратитесь к врачу незамедлительно!!!", reply_markup=markup)

    elif message.text == "Ничего не вижу":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Странно что вы здесь! Самолечение не допустимо! Обратитесь к врачу незамедлительно!!!", reply_markup=markup)

    elif message.text == "Появилась сыпь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn12 = types.KeyboardButton("Спасибо")
        btn13 = types.KeyboardButton("Другие жалобы")
        markup.add(btn12, btn13)
        bot.send_message(message.chat.id, "Если сыпь сопровождается температурой, то необходимо обратится к врачу-инфекционисту. Если сыпь появилась на прием лекарств или пищу, не сопровождается отеком и удушьем, то можно использовать любой антигистаминный препарат (самый простой супрастин). Если появился отек и стало тяжело дышать, то вызываем скорую незамедлительно!!!", reply_markup=markup)

    elif message.text == "Спасибо":
        bot.send_message(message.chat.id, "Выздоравливайте! В начало - /start")

    elif message.text == "Другие жалобы":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Температура выше 38,5С")
        btn2 = types.KeyboardButton("Болит горло")
        btn3 = types.KeyboardButton("Болит зуб")
        btn4 = types.KeyboardButton("Болит живот")
        btn5 = types.KeyboardButton("Болит голова")
        btn6 = types.KeyboardButton("Диарея")
        btn7 = types.KeyboardButton("Насморк")
        btn8 = types.KeyboardButton("Тошнит")
        btn9 = types.KeyboardButton("Упал и кажется что-то не так")
        btn10 = types.KeyboardButton("Ничего не вижу")
        btn11 = types.KeyboardButton("Появилась сыпь")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_message(message.chat.id, "Уточните жалобы", reply_markup=markup)


def main():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    main()