# Instagram Followers Bot 😊

This is a simple Telegram bot built with Python using the aiogram library to fetch the list of followers of a given Instagram user.

## 🛠️ Setup

1. **Clone this repository:**

    ```bash
    git clone https://github.com/yourusername/instagram-followers-bot.git
    ```

2. **Install the required dependencies:**

3. **Create a Telegram bot and get the API token from the BotFather.**

4. **Create an Instagram account for the bot and note down the username and password.**

5. **Update the `config.py` file with your Telegram bot token, Instagram username, and Instagram password.**

## 🚀 Usage

1. **Start the bot by running:**

    ```bash
    python main.py
    ```

2. **Interact with the bot in your Telegram app:**

    - Start the bot by sending `/start`.
    - Get the list of followers by sending `/followers <username>` where `<username>` is the Instagram username of the user whose followers you want to fetch.

3. **Enjoy exploring Instagram followers right from your Telegram! 🎉**

## 📝 Notes

- The bot has a rate limit of 2 requests per minute to avoid hitting Instagram's API rate limits.
- If the Instagram profile is private, the bot will notify that the profile is private.
- If the Instagram profile does not exist, the bot will notify that the profile does not exist.

