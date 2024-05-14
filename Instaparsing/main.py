import asyncio
from aiogram import Bot, Dispatcher, types
import time

# Глобальные переменные для отслеживания времени запросов
last_request_time = 0
request_count = 0
MAX_REQUESTS_PER_MINUTE = 2

bot = Bot(token="YOUR_BOT_TOKEN")
dp = Dispatcher()

import instaloader

async def get_followers(username, limit=200):
    global last_request_time, request_count
    
    # Проверяем, сколько времени прошло с момента последнего запроса
    current_time = time.time()
    if current_time - last_request_time < 60:  # 60 секунд в минуте
        request_count += 1
        if request_count > MAX_REQUESTS_PER_MINUTE:
            return "Слишком много запросов за минуту!"
    else:
        # Сбрасываем счетчик запросов, если прошла минута с момента последнего запроса
        last_request_time = current_time
        request_count = 1

    # Create an instance of the Instaloader class
    loader = instaloader.Instaloader()
    loader.login("YOUR_INSTAGRAM_USERNAME", "YOUR_INSTAGRAM_PASSWORD")

    try:
        # Load the user's profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Check if the profile is private
        if profile.is_private:
            return f"Профиль '{username}' является закрытым."

        # Get the list of followers
        followers = []
        count = 0
        for follower in profile.get_followers():
            followers.append(follower.username)
            count += 1
            if count >= limit:
                break

        # Check if there are no followers
        if not followers:
            return f"У пользователя {username} нет подписчиков."

        followers_str = "\n".join(followers)
        return f"Подписчики пользователя {username}:\n{followers_str}"

    except instaloader.exceptions.ProfileNotExistsException:
        return f"Профиль с именем '{username}' не существует."
    except Exception as e:
        return f"Произошла ошибка: {e}"

@dp.message(commands=['start'])
async def start(message: types.Message):
    await message.answer("Привет! Я бот, который поможет тебе получить список подписчиков Instagram. "
                         "Для этого используй команду /followers <имя_пользователя>.")

@dp.message(commands=['followers'])
async def followers(message: types.Message):
    try:
        # Split message text and extract the username
        _, username = message.text.split(' ', 1)
        followers_list = await get_followers(username)
        await message.answer(followers_list)
    except ValueError:
        # If splitting fails due to insufficient arguments
        await message.answer("Использование: /followers <имя_пользователя>")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
