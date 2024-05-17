## Project Overview
Project Name: Telegram Bot <br>
Author: Priyanshu K Sharma <br>
## Description: <br>
This is a Telegram bot created using the python-telegram-bot library. The bot responds to various commands and messages from users, providing information and assistance.<br>

## Program Structure:
The program consists of a Python script named tele-bot.py.
It utilizes the python-telegram-bot library for interacting with the Telegram Bot API.
The program reads the Telegram bot token from the environment variable TOKEN using the python-dotenv library.
It defines several functions to handle different commands and messages received from users:<br>

start:<br>
Sends a welcome message to users when they start a conversation with the bot.<br>
helps: <br>
Provides information about the available commands and how to use them.<br>
content: <br>
Sends information about the author, including name, age, degree, college, semester, and year.<br>
contact: <br>
Provides links to the author's LinkedIn and GitHub profiles.<br>
handle_message: <br>
Handles messages that do not match any of the predefined commands.<br>
The program sets up an Updater and a Dispatcher to handle incoming updates from Telegram.<br>
It adds handlers for various commands and messages using CommandHandler and MessageHandler.<br>
Finally, it starts the bot by calling start_polling() and enters the idle state.

## Repository Structure:<br>
telegram-bot/<br>
│<br>
├── tele-bot.py<br>
├── requirements.txt<br>
└── README.md<br>

## Usage

1. Start a conversation with the bot by sending a message. <br>
2. Use the following commands to interact with the bot:<br>
    - `/start`: Start a conversation with the bot.<br>
    - `/help`: Get help and information about available commands.<br>
    - `/content`: Get information about the author.<br>
    - `/contact`: Get contact information of the author.<br>

## Installation

1. Clone the repository: <br>
   ```bash
   git clone https://github.com/your_username/telegram-bot.git

2. Install dependencies: <br>
    ```bash
    pip install -r requirements.txt

3. Set the TOKEN environment variable with your Telegram bot token.<br>

4. Run the bot:<br>
    ```bash
    python tele-bot.py
