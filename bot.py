import os
import telebot
from google import genai

TG_TOKEN = os.environ["TG_TOKEN"]
GEMINI_KEY = os.environ["GEMINI_KEY"]

bot = telebot.TeleBot(TG_TOKEN)
client = genai.Client(api_key=GEMINI_KEY)

MODELS = ["gemini-3.5-flash", "gemini-3.8-flash", "gemini-2.5-flash"]

@bot.message_handler(func=lambda m: True)
def reply(message):
    for model in MODELS:
        try:
            r = client.models.generate_content(model=model, contents=message.text)
            bot.reply_to(message, r.text)
            return
        except Exception as e:
            print(model, "ошибка:", e)
    bot.reply_to(message, "Gemini сейчас перегружен, попробуйте через минуту.")

bot.infinity_polling()
