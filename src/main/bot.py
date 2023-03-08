import os
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Hi {message.from_user.first_name}, how can I help you today?'
        )

@bot.message_handler(commands=['echo'])
def send_echo(message):
    if (len(message.text) < 6):
        bot.send_message(chat_id=message.chat.id, text="Nothing to echo")
        return
    text = message.text[6:] 
    bot.reply_to(message, text)

bot.infinity_polling()