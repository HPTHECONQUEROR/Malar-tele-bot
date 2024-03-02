# Malar Telegram Bot

## Introduction
Malar Telegram Bot is a chatbot implemented in Python using the Telegram Bot API and Hugging Face's text generation model. The bot simulates conversations with users on the Telegram messaging app, responding to their messages in a polite and engaging manner.

## Installation
Before running the bot, ensure you have installed the required dependencies by executing the following command:
```bash
pip install -r requirements.txt
```

## Getting Started
1. **Get Telegram Bot Token**: 
   - Create a new bot on Telegram by talking to [BotFather](https://core.telegram.org/bots#6-botfather).
   - Follow the instructions provided by BotFather to obtain your bot token.

2. **Get Hugging Face API Key**:
   - Sign up for an account on the [Hugging Face website](https://huggingface.co/login).
   - After logging in, navigate to your profile settings and locate your API key.
   
3. **Configure Credentials**:
   - Replace `YOUR_BOT_TOKEN` in `main.py` with your Telegram bot token obtained from BotFather.
   - Replace `"YOUR_KEY"` in `response.py` with your Hugging Face API key.

## Usage
- Run the bot by executing `python main.py` in your terminal.
- Start chatting with the bot on Telegram by sending messages to the bot's username.

## Features
- Simulates conversations with users in a polite and engaging manner.
- Responds to user messages with generated text based on Hugging Face's text generation model.
- Handles emoji messages and responds accordingly.
- Warns users against inappropriate behavior.

## Contributors
- [Hari Prasath AS]([https://github.com/HPTHECONQUEROR/])

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
