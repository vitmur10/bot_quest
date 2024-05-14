from aiogram.types import Message
from const import *


# Функція для входу в систему з різними рівнями доступу
async def login(password: str):
    global current_access_level
    # Перевірка правильності пароля
    for level, passwd in PASSWORDS.items():
        if password == passwd:
            current_access_level = ACCESS_LEVELS[level]
            return f"Ви увійшли з рівнем доступу: {level}."
    return "Невірний пароль. Спробуйте ще раз."


# Обробник команди /login, що дозволяє користувачам ввійти з різними рівнями доступу
@dp.message_handler(commands=['login'])
async def login_command(message: Message):
    global current_access_level
    # Перевірка формату повідомлення
    if len(message.text.split()) != 2:
        await message.answer("Неправильний формат. Використовуйте '/login рівень_доступу'.")
        return

    # Витягуємо рівень доступу з команди
    _, password = message.text.split()

    # Викликаємо функцію входу
    result = await login(password)
    await message.answer(result)


# Обробник команди /admin_command, доступ до якої мають тільки адміністратори
@dp.message_handler(commands=['admin_command'])
async def admin_command(message: Message):
    global current_access_level
    if current_access_level >= ACCESS_LEVELS["admin"]:
        await message.answer("Ця команда доступна тільки адміністраторам.")
    else:
        await message.answer("У вас недостатньо прав для виконання цієї команди.")


# Обробник команди /moderator_command, доступ до якої мають тільки модератори і адміністратори
@dp.message_handler(commands=['moderator_command'])
async def moderator_command(message: Message):
    global current_access_level
    if current_access_level >= ACCESS_LEVELS["moderator"]:
        await message.answer("Ця команда доступна модераторам і адміністраторам.")
    else:
        await message.answer("У вас недостатньо прав для виконання цієї команди.")


# Обробник для інших повідомлень
@dp.message_handler()
async def echo(message: Message):
    await message.answer("Я не розумію цю команду. Введіть /help, щоб отримати допомогу.")


# Запускаємо бота
if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())
    loop.close()
