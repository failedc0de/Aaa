import asyncio
import importlib
import re
from contextlib import closing, suppress
from uvloop import install
from pyrogram import filters, idle
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)
from zentech import (
    app,
    aiohttpsession
)
from zentech.Manager import ALL_MODULES
from zentech.utils import paginate_modules
loop = asyncio.get_event_loop()

flood = {}
HELPABLE = {}

async def start_bot():
    global HELPABLE

    for module in ALL_MODULES:
        imported_module = importlib.import_module("zentech.userbot." + module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.replace(" ", "_").lower()
                ] = imported_module

    all_module = ""
    j = 1
    for i in ALL_MODULES:
        if j == 1:
            all_module += "•≫ Successfully imported:{:<15}.py\n".format(i)
            j = 0
        else:
            all_module += "•≫ Successfully imported:{:<15}.py".format(i)
        j += 1   
    await idle()
    await aiohttpsession.close()
    print("Stopping clients")
    await app.stop()
    print("Cancelling asyncio tasks")
    for task in asyncio.all_tasks():
        task.cancel()
    print("Bot offline")

help_text = """
**Help module

Prefixes: `!` `$`**"""

async def help_parser(name, keyboard=None):
    if not keyboard:
        help_keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (help_text,help_keyboard)

@app.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(client,CallbackQuery):
    text ,help_keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.edit_message_text(text="**Help module**\n\n**Prefixes:** `!` `$`",reply_markup=help_keyboard,disable_web_page_preview=True)

@app.on_callback_query(filters.regex("opebn_back"))
async def opebn_back(client,CallbackQuery):
    await CallbackQuery.edit_message_text(text="**Klik Open**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open", callback_data="bot_commands")]]), disable_web_page_preview=True)

@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query: CallbackQuery):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = "**Help module**\n\n**Prefixes:** `!` `$`"
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = (
            "Document for **{}**:\n".format(
                HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__)
        if hasattr(HELPABLE[module], "__helpbtns__"):
                       button = (HELPABLE[module].__helpbtns__) + [[InlineKeyboardButton("Back", callback_data="bot_commands")]]
        if not hasattr(HELPABLE[module], "__helpbtns__"): button = [[InlineKeyboardButton("Back", callback_data="bot_commands")]]
        await query.edit_message_text(text=text,reply_markup=InlineKeyboardMarkup(button),disable_web_page_preview=True,)
    elif home_match:
        await query.edit_message_text(query.from_user.id,text="PM saya jika Anda memiliki pertanyaan bagaimana menggunakan saya!",reply_markup=var.home_keyboard_pm)
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.edit_message_text(text=top_text,reply_markup=InlineKeyboardMarkup(paginate_modules(curr_page - 1, HELPABLE, "help")),disable_web_page_preview=True)
    elif next_match:
        next_page = int(next_match.group(1))
        await query.edit_message_text(text=top_text,reply_markup=InlineKeyboardMarkup(paginate_modules(next_page + 1, HELPABLE, "help")),disable_web_page_preview=True)
    elif back_match:
        await query.edit_message_text(text=top_text,reply_markup=InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help")),disable_web_page_preview=True)
    elif create_match:
        text, keyboard = await help_parser(query)
        await query.edit_message_text(text=text,reply_markup=keyboard,disable_web_page_preview=True)
    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    install()
    with closing(loop):
        with suppress(asyncio.exceptions.CancelledError):
            loop.run_until_complete(start_bot())
        loop.run_until_complete(asyncio.sleep(1.0))
