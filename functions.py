from aiogram.types import Message
from aiogram import Bot
from pprint import pprint as print
import requests


async def answer(message : Message, bot : Bot):
    url = "https://v6.exchangerate-api.com/v6/d49f1bb649b9321048c66e8a/latest/USD"
    data = requests.get(url)
    data = data.json()
    text = "Amerika summasi boshqa pul birliklarida : "
    # print(data['conversion_rates'])
    # print(type(data['conversion_rates']))
    await bot.send_chat_action(chat_id = message.chat.id, action="typing")
    for i, j in (data['conversion_rates']).items():
        text += f"\n👉 {i} : {j}"
    
    await message.answer(text)
