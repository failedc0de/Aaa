from pyrogram import Client, filters
from zentech import *
from zentech.__main__ import *
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery,
)
import asyncio
import os
import time
from typing import List
from datetime import datetime

lengths = 200

IMG = "https://telegra.ph/file/0cec1aa4321d60b2c93fc.jpg"

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



@app.on_callback_query(filters.regex("cbsaastart"))
async def cbsaastart(_, query: CallbackQuery):
    start_time = time.time()
    anjayy = await query.edit_message_text("⚡️",
                                           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="bot_commands")]])
                                          )
    end_time = time.time()
    telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ms"
    uptime = get_readable_time((time.time() - StartTime))
    await asyncio.sleep(1)
    await query.edit_message_text(f"**🏓 Pong!!\n\n➤ Uptime : `{uptime}`\n➤ Pinger : `{telegram_ping}`**",
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Back", callback_data="backpingse")]])
                                 )
@app.on_callback_query(filters.regex("backpingse"))
async def backpingse(_, query: CallbackQuery):
    await query.edit_message_text(f"<b>➖➖➖➖➖➖➖➖➖➖\n         ⚡️ Vantex - Userbot ⚡️\n➖➖➖➖➖➖➖➖➖➖\n➤ Owner : {query.from_user.mention}\n➤ Modules : <code>20 Modules</code>\n➤ Bot Version : <code>1.7.0@vantex</code>\n➤ Python Version : <code>3.10.8</code>\n➤ Pyrogram Version : <code>2.0.59</code></b>",
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Ping", callback_data="cbsaastart")]]),
                                 )
    
VANTEX_TEXT = """
<b>➖➖➖➖➖➖➖➖➖➖➖➖➖
                            Vantex-Userbot                            
➖➖➖➖➖➖➖➖➖➖➖➖➖
👮🏻‍♀️ Order Vantex userbot sekarang!!

➤ Simpel
➤ Ga ribet
➤ cepat
➤ Tanpa akun heroku

minat? pc @phobiakalian</b>"""
@app.on_inline_query()
async def wishper_ai(_, sz: InlineQuery):
    query = sz.query
    user_mention = sz.from_user.mention
    split = query.split(' ', 1)
    if query == '':
        title = f"  Order"
        content = VANTEX_TEXT
        description = "Deploy vantex Userbot"
        button2 = InlineKeyboardButton(
            "👮🏻‍♀️ Contact",
            url="https://t.me/phobiakalian"
        )
        switch_pm_text = f"klik disini untuk order vantex userbot"
        switch_pm_parameter = "buy"
        await sz.answer(
            results=[
                InlineQueryResultArticle(
                    title=title,
                    input_message_content=InputTextMessageContent(content),
                    description=description,
                    thumb_url=IMG,
                    reply_markup=InlineKeyboardMarkup([[button2]])
                )
            ],
        )
    elif query == "helprtnk":
        title = f"❓ help"
        content = ("**➖➖➖➖➖➖➖\n    🌐 Click Open 🌐\n➖➖➖➖➖➖➖**""")
        description = "Untuk melihat semua bantuan"
        button2 = InlineKeyboardButton(
            "Open",
            callback_data="bot_commands"
        )
        switch_pm_text = f"klik disini untuk order vantex userbot"
        switch_pm_parameter = "buy"
        await sz.answer(
            results=[
                InlineQueryResultArticle(
                    title=title,
                    input_message_content=InputTextMessageContent(content),
                    description=description,
                    thumb_url=IMG,
                    reply_markup=InlineKeyboardMarkup([[button2]])
                )
            ],
        )
    elif query == "adnkei":
        title = "alive"
        content = f"<b>➖➖➖➖➖➖➖➖➖➖\n         ⚡️ Vantex - Userbot ⚡️\n➖➖➖➖➖➖➖➖➖➖\n➤ Owner : {sz.from_user.mention}\n➤ Modules : <code>20 Modules</code>\n➤ Bot Version : <code>1.7.0@vantex</code>\n➤ Python Version : <code>3.10.8</code>\n➤ Pyrogram Version : <code>2.0.59</code></b>"
        description = "Untuk melihat detail vantex userbot"
        button1 = InlineKeyboardButton(
            "Ping",
            callback_data="cbsaastart"
        )
        switch_pm_text = f"klik disini untuk order vantex userbot"
        switch_pm_parameter = "ayee"
        await sz.answer(
            results=[
                InlineQueryResultArticle(
                    title=title,
                    input_message_content=InputTextMessageContent(content),
                    description=description,
                    thumb_url=IMG,
                    reply_markup=InlineKeyboardMarkup([[button1]])
                )
            ],
        )
