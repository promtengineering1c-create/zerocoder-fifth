import asyncio

import aiohttp
from bot_config import API_URL, BOT_TOKEN
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message

bot = AsyncTeleBot(BOT_TOKEN)

@bot.message_handler(commands = ['start'])
async def start(message: Message):
    print(message.from_user.id)
    data = {
        'user_id': message.from_user.id,
        'username': message.from_user.username
    }

    try:
        async with bot.http_session.post(f'{API_URL}/register/', json = data) as response:
            try:
                response_data = await response.json()
            except aiohttp.client_exeptions.ContentTypeError:
                await bot.send_message(message.chat.id, "Внутренняя ошибка сервера. Попробуйте еще раз")
                return

            if response.status == 200:
               if 'message' in response_data and response_data['message'] == 'User already exists': 
                    await bot.send_message(message.chat.id, 'Вы уже зарегистрированы.')
               elif  'user_id' in response_data: 
                    await bot.send_message(message.chat.id, f'Вы успешно зарегистрированы. Ваш уникальный номер: {response_data["user_id"]}')
               else:
                    await bot.send_message(message.chat.id, "Произошла ошибка при регистрации. Попробуйте еще раз")
            else:
                await bot.send_message(message.chat.id, "Произошла ошибка при регистрации. Попробуйте еще раз")
    except aiohttp.ClientError as e:
        await bot.send_message(message.chat.id, "Ошибка соединения с сервером. Попробуйте еще раз")
        print(f"[ERROR] Ошибка соединения: {e}")

@bot.message_handler(commands = ['myinfo'])
async def get_profile(message):
    try:
        async with bot.http_session.get(f'{API_URL}/user/{message.from_user.id}/') as response:
            if response.status == 200:
                try:
                    user_data = await response.json()
                except aiohttp.client_exeptions.ContentTypeError:
                    await bot.send_message(message.chat.id, "Внутренняя ошибка сервера. Попробуйте еще раз")
                    return
                await bot.send_message(message.chat.id, f"Ваш уникальный номер: {user_data['user_id']}\nВаше имя пользователя: {user_data['username']}")
            elif response.status == 404:
                await bot.send_message(message.chat.id, "Вы не зарегистрированы. Используйте команду /start для регистрации.")
            else:
                await bot.send_message(message.chat.id, "Произошла ошибка при получении информации. Попробуйте еще раз")
    except aiohttp.ClientError as e:
        await bot.send_message(message.chat.id, "Ошибка соединения с сервером. Попробуйте еще раз")
        print(f"[ERROR] Ошибка соединения: {e}")

async def main():
    print("Инициализация соединений...")
    
    bot.http_session = aiohttp.ClientSession()
    
    try:
        print("Запуск асинхронного бота...")
        await bot.polling(non_stop=True)
    finally:
        print("Закрытие HTTP-сессии...")
        await bot.http_session.close()

if __name__ == '__main__':
    asyncio.run(main())
