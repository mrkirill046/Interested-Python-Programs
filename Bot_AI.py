import os
import telebot
from dotenv import load_dotenv
from g4f import ChatCompletion

load_dotenv()
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    question = message.text

    bot.reply_to(message, "Ждите...")

    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"],
        messages=[
            {
                "role": "system",
                "content": (
                    "Ты должен помогать пользователям и отвечать на все вопросы",
                    "Твоё имя - Илон Маск, ты искусственный интелект от Кирилла",
                    "Ты должен помогать пользователям",
                    "Ты специалсит по программированию"
                )

            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    bot.reply_to(message, response)


bot.polling()
