from aiogram import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

cfg = {
    'token': '6075826339:AAF-yGH627OMzQcZAQuQes0PC3K3dB3PUd4',
    'db_name': 'bd',

    'button_new_question': '✉ Поставити питання',

    'welcome_message': "Вітаю, студент КНУТД❗️🧑‍🎓\n"
                       "Завжди виникає безліч запитань💭\n"
                       "Тут ти знайдеш необхідну інформацію, яка допоможе тобі отримати відповіді на найпоширеніші "
                       "запитання🔍\n ",
    'error_message': 'Упс! Помилка! Не хвилюйтеся, помилку вже відправлено розробникам.',
    'ban_message': '⚠ Ви заблоковані в боті!',
}
bot = Bot(token=cfg['token'])


logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot, storage=MemoryStorage())

# Паролі для різних рівнів доступу
PASSWORDS = {
    "user": "user_password",
    "moderator": "moderator_password",
    "admin": "admin_password"
}

# Рівні доступу користувачів
ACCESS_LEVELS = {
    "user": 0,
    "moderator": 1,
    "admin": 2
}

# Початковий рівень доступу для користувачів
DEFAULT_ACCESS_LEVEL = ACCESS_LEVELS["user"]

# Змінна, що показує рівень доступу поточного користувача
current_access_level = DEFAULT_ACCESS_LEVEL


""""start" - Я бот створений допомогти вам викрити тайну таємного інженера, та знайти бокси.
У мене обмеженний функціонал, щоб мною користуватися вам потрібно розшифровуння текстів, та розв'язок задач. А до мене вам  потрібно вписати результат. 

 /"розшифрований текст"

Після чого я можу дати підсказку куди рухатися далі

У вас є можливість найти 3 бокси, різних рівней складності 

/prime - Простий
/average - Середній
/arduous - Тяжкий

Виберіть свій рівень, після чого я вас направлю по вашому вибраному шляху, щоб ви могли дійти до своєї цілі, та знайти бокси. Бажаю вам успіху!"""