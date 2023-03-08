import os
from dotenv import load_dotenv
import telebot
import openai

load_dotenv()

openai.api_key = os.environ.get("CODEX_API_KEY")

def request(prompt):
    body = {
      "model": "code-davinci-002",
      "prompt": prompt,
      "max_tokens": 100,
      "temperature": 0,
    }
    print("... Requesting output ...\n")
    response = openai.Completion.create(**body)
    try:
        result = response["choices"][0]["text"]
        return result
    except:
        return "Can't get the result"


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

@bot.message_handler(commands=["code"])
def send_code(message):
    if (len(message.text) < 6):
        bot.send_message(chat_id=message.chat.id, text="Nothing to write about")
        return
    prompt = message.text[6:]
    output = request(prompt)
    bot.send_message(chat_id=message.chat.id, text=output)

@bot.message_handler(commands=["python"])
def send_code(message):
    if (len(message.text) < 6):
        bot.send_message(chat_id=message.chat.id, text="Nothing to write about")
        return
    prompt = '"""\n' + message.text[6:] + '\n"""'
    output = request(prompt)
    bot.send_message(chat_id=message.chat.id, text=output)

bot.infinity_polling()