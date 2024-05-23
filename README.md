<h1 align="left">Телеграм бот - NikitaBot / Telegram bot - NikitaBot</h1>
<h3 align="left">RU</h3>
Этот репозиторий содержит моего первого телеграм бота, который может делать заметки, вычисления, кидать мемы и кое-как отвечать на обычные сообщения.<br />
Сам бот написан на Telobot API - библиотеки, которая даёт возможность создавать телеграм ботов на Python.
<h3 align="left">EN</h3>
This repository contains the code of my very first telegram bot, which can take notes, do some basic calculations, send you memes and somewhat respond to your messages.<br />
This bot have been made with Telobot API - library made for creating telegram bots on Python.

<h1 align="left">Как запустить? / How to run your bot? </h1>
<h3 align="left">RU</h3>
Чтоб запустить бота, нужно сделать следующее:<br />
1. Клонировать репозиторий(делается в консоли)<br />
- git clone https://github.com/Muxa3/NikitaBot.git<br />
- cd NikitaBot<br /><br />
2. Установить некоторые библиотеки для работы(тоже в консоли):<br />
- pip install pyTelegramBotAPI<br />
- pip install sympy
<h3 align="left">EN</h3>
You need to do the following:<br />
1. Clone this repository(run commands in console)<br />
- git clone https://github.com/Muxa3/NikitaBot.git<br />
- cd NikitaBot<br /><br />
2. Download some required libraries(also in console):<br />
- pip install pyTelegramBotAPI<br />
- pip install sympy

<h1 align="left">Токены / Tokens</h1>
<h3 align="left">RU</h3>
Для работы боту помимо библиотек нужен свой токен.<br />
Если токена у вас нет, вы можете его создать при помощи BotFather в телеграме.<br />
Для этого нужно сделать следующее:<br />
1. Открыть телеграм и найти бота - BotFather.<br />
2. Начнити чат с BotFather и используйте команду /newbot.<br />
3. BotFather попросит имя для бота - назовите как хотите.<br />
4. BotFather также спросит про никнейм для бота - назовите как хотите, в пределах правил (Ник должен кончаться на "bot" по типу "NikitaBot").<br />
5. После этого BotFather создаст бота и даст токен - его надо сохранить.
<h3 align="left">EN</h3>
In addition to libraries, for this bot to function properly, it needs a token.<br />
If you dont have you, create it with help of BotFather in telegram.<br />
For this you need to do the following:<br />
1. Open telegram and find bot with this name - BotFather.<br />
2. Start a chat with BotFather and use /newbot command.<br />
3. BotFather would ask you for your new bot's name - name however you want.<br />
4. BotFather would also ask for bot's username - give it any, but it should end with "bot" (for example "NikitaBot").<br />
5. After all of that BotFather will create a new bot and provide you with its token - you should copy it.

<h1 align="left">Настройка / Setting Up</h1>
<h3 align="left">RU</h3>
Откройте main.py file и вставьте свой токен за место комментария<br /><br />

token=#Вставьте сюда свой Токен<br />
v v v<br />
token=abcd1233 (как пример)
<h3 align="left">EN</h3>
Open main.py file and insert your token into placeholder<br /><br />

token=#Вставьте сюда свой Токен<br />
v v v<br />
token=abcd1233 (as example)

<h1 align="left">Запуск / Launch</h1>
<h3 align="left">RU</h3>
Запустить бота можно через команду:<br /><br />

python main.py
<h3 align="left">EN</h3>
You can run your bot through console command:<br /><br />

python main.py

<h1 align="left">Функционал / Features</h1>
<h3 align="left">RU</h3>
- В ответ на комманды /start и /help отправляет приветствие.<br />
- В ответ на сообщения "Привет" и "Я скучаю" отправляет свои приколюхи, на остальное - отвечает "Ага-ага".<br />
- Кнопка "Мемы" - отправляет случайный мем-картинку на английском с сайтика.<br />
- Кнопка "Вычисления" - попросит математический пример и решит его по логике Python.<br />
- Кнопка "Заметки" - сделает заметку, о которой напомнит позже.
<h3 align="left">EN</h3>
- Responds to /start and /help with welcome message.<br />
- Responds to phrases like "Привет" and "Я скучаю", otherwise it would respond with "Ага-ага".<br />
- Button "Мемы" - sends you a random meme image from specified site.<br />
- Button "Вычисления" - does some basic arithmetic operations.<br />
- Button "Заметки" - creates a note that it would notify you of in due time.


<h1 align="left">На заметку / Disclaimer</h1>
<h3 align="left">RU</h3>
Бот синхронный и функция заметок, а именно таймера, была сделана мягко говоря некорректно<br />
- поэтому этот бот не рассчитан на большой трафик.
<h3 align="left">RU</h3>
This bot works synchronously, and its note-taking function, in particular, the timer function, was made poorly<br />
- because of that it cannot handle alot of traffic.