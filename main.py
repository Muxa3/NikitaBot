import telebot
from telebot import types
from urllib.request import urlopen
import sympy
import datetime
import threading


token=#Вставьте сюда свой Токен

#Инициализируем бота
bot=telebot.TeleBot(token)


#Стартовое меню, которое отвечает на команды /help и /start
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = "Мемы", callback_data='meme')
    button2 = types.InlineKeyboardButton(text = "Вычисления", callback_data='calc')
    button3 = types.InlineKeyboardButton(text = "Заметки", callback_data='note')
    markup.add(button1, button2, button3)
    bot.send_message(chat_id=message.chat.id,text="Привет, {0.first_name} ✌️\nМеня зовут Никита и я твой личный робо-ботик❤️".format(message.from_user), reply_markup=markup)


#Обработчик кнопки 'Мемы' - кидает случайный мем с https://img.randme.me/
@bot.callback_query_handler(func=lambda call: call.data =="meme")
def meme_pressed(call: types.CallbackQuery):
    bot.reply_to(message=call.message, text="Ща кину)")
    bot.send_photo(call.message.chat.id, urlopen('https://img.randme.me/'))


#Обработчик кнопки 'Вычисления' - запрашивает у пользователя пример для решения
@bot.callback_query_handler(func=lambda call: call.data =="calc")
def calc_pressed(call: types.CallbackQuery):
    bot.reply_to(message=call.message, text="А ну ка, дай мне примерчик")
    #берет следующее сообщение пользователя и кидает его на метод process_calc
    bot.register_next_step_handler(call.message, process_calc)

#Метод для вычислений
def process_calc(message):
    try:
        result = int(sympy.simplify(message.text))
        bot.send_message(message.chat.id, text=result)
    #если выскакивает ошибка - кидает сообщение
    except:
        bot.reply_to(message, text = 'Блин, я такое не вычислю... Исправляй')


#Обработчик кнопки 'Заметки' - запрашивает у пользователя название для заметки
@bot.callback_query_handler(func=lambda call: call.data =="note")
def note_pressed(call: types.CallbackQuery):
    bot.reply_to(message=call.message, text="Лады)")
    bot.send_message(call.message.chat.id, "А о чём напомнить?")
    #берет следующее сообщение пользователя и кидает его на метод set_note_name
    bot.register_next_step_handler(call.message, set_note_name)

#Метод, заполняет в словарь название заметки и выпрашивает для неё дату
def set_note_name(message):
    user_data = {}
    user_data[message.chat.id] = {'note_name': message.text}
    bot.send_message(message.chat.id, 'Ага, понял... А тебе когда напомнить? Ну, знаешь в формате ГГГГ-ММ-ДД чч:мм:сс.')
    #берет следующее сообщение пользователя и кидает его на метод set_note_date
    bot.register_next_step_handler(message, set_note_date, user_data)

#Метод, которые выполняет обработку предоставленной даты и запускает таймер
def set_note_date(message, user_data):
    try:
        note_date = datetime.datetime.strptime(message.text, '%Y-%m-%d %H:%M:%S')
        now = datetime.datetime.now()
        delta = note_date - now
        #если дата уже прошла - кидает сообщение
        if delta.total_seconds() <= 0:
            bot.send_message(message.chat.id, 'Так прошло же время уже...')
            bot.send_message(message.chat.id, 'Крч, давай по новой')
        else:
            note_name = user_data[message.chat.id]['note_name']
            bot.send_message(message.chat.id, 'Окей, так и запишем... "{}" на {}.'.format(note_name, note_date))
            bot.send_message(message.chat.id, 'Потом обязательно напомню)')
            #Создание таймера
            note_date = threading.Timer(delta.total_seconds(), notify, [message.chat.id, note_name])
            note_date.start()
    #если выскакивает ошибка - кидает сообщение
    except:
        bot.send_message(message.chat.id, 'Я не понял когда...')
        bot.send_message(message.chat.id, 'Крч, давай по новой')

#Метод, к которому обращается таймер для отправки напоминания
def notify(chat_id, note_name):
    bot.send_message(chat_id, 'Эй, пора "{}"!'.format(note_name))


#Эхо-бот
@bot.message_handler(func=lambda message: True)
def message_reply(message):
    text = message.text.lower()
    text = ' '.join(text.split())
    if text=='я скучаю':
        bot.send_message(message.chat.id,"Я тоже соскучился, сладкий 💋")
        bot.send_photo(message.chat.id, 'https://imgur.com/a/SbaXpJY')
    elif text=='привет':
        bot.send_message(message.chat.id,"Тебе тоже привет, пупсик)")
    else:
        bot.send_message(message.chat.id,"Ага-ага")

bot.infinity_polling()