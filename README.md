# Telegram Bot

This project is a simple Telegram bot built with Python. The bot responds to user commands and provides information about the creator, Priyanshu K Sharma. It is containerized using Docker for easy deployment.

## Features

- Responds to `/start` with a welcome message
- `/help` provides a list of available commands and their descriptions
- `/content` shares information about the creator
- `/contact` provides contact links (LinkedIn, GitHub)
- Handles unrecognized messages with a default response

## Commands

| Command    | Description                                      |
|------------|--------------------------------------------------|
| /start     | Start a conversation with the bot                |
| /help      | List available commands and their usage          |
| /content   | Information about Priyanshu K Sharma             |
| /contact   | Contact information (LinkedIn, GitHub)           |

## Getting Started

### Prerequisites

- Python 3.9+
- Telegram account (to create a bot and get a token)

### Installation

1. **Clone the repository:**
    ```sh
    git clone <repo-url>
    cd Telegram_Bot
    ```

2. **Set up virtual environment:**
    ```sh
    # Install venv if not available
    sudo apt install python3.12-venv
    
    # Create virtual environment
    python3 -m venv venv
    
    # Activate virtual environment
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirement.txt
    ```

4. **Set up environment variables:**
    - Create a `.env` file in the project root:
      ```env
      TOKEN=your_telegram_bot_token_here
      ```

5. **Run the bot:**
    ```sh
    python tele-bot.py
    # or
    ./venv/bin/python tele-bot.py
    ```

## Docker Usage

You can run the bot inside a Docker container:

1. **Build the Docker image:**
    ```sh
    docker build -t telegram_bot:latest .
    ```

2. **Run the container:**
    ```sh
    docker run --env-file .env telegram_bot:latest
    ```

## Project Structure

```
.
├── Dockerfile
├── README.md
├── requirement.txt
├── tele-bot.py
└── telegram_bot/
     └── README.md
```

## Troubleshooting

If you encounter a `ValueError: 'token' or 'bot' must be passed` error when running the bot in Docker, ensure the following:

- The `.env` file contains your token as `TOKEN=your_token_here` (no quotes).
- The Docker image is rebuilt after any changes to `.env` or code:
    ```sh
    docker build -t telegram_bot .
    ```
- The container is run with the environment file:
    ```sh
    docker run --env-file .env telegram_bot
    ```
- The code uses `os.environ.get("TOKEN")` (not `load_dotenv()`) to read the token. This ensures the token is read from Docker's environment variables.

If you need to update your code, make sure to remove or comment out any `load_dotenv()` lines and use only `os.environ.get("TOKEN")` for reading the token.

---

## Credits

Created by Priyanshu K Sharma

- [LinkedIn](https://www.linkedin.com/in/priyanshu-kumar-sharma-333800251/)
- [GitHub](https://github.com/PriyanshuKSharma)

---
Feel free to contribute or raise issues!
