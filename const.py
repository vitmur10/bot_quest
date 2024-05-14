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