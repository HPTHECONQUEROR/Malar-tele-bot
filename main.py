import telebot
from Response import RunBot
import threading
import os

BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

user_instances = {}


def get_user_file(user_id, first_name):
    file_path = f"{user_id}.txt"
    if not os.path.exists(file_path):
        file_path = f"{first_name}.txt"

    return file_path


def handle_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name


    if user_id not in user_instances:
        file_path = get_user_file(user_id, first_name)
        user_instances[user_id] = RunBot(file_path, first_name)
    command = message.text
    print("given message\n"+command)
    try:
        reply_message = user_instances[user_id].bot_output(command)

    except:
        reply_message = "Sorry to say this, but i gotta sleep now!"
    bot.reply_to(message, reply_message)
    print("REPLYMESSAGE\n"+reply_message)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    threading.Thread(target=handle_user, args=(message,), daemon=True).start()

bot.polling()
