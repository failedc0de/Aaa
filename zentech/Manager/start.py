from pyrogram import Client, idle, filters
from pyrogram.types import Message


@Client.on_message(filters.private & filters.command("start"))
async def start_bot(_, ctx: Message):
    form = await _.send_message(ctx.chat.id, f"hello")
    
@Client.on_message(filters.private & filters.command("form"))
async def form_bot(_, ctx: Message):
    try:
        cek = await ctx.chat.ask("Type your string session")
        await _.send_message(ctx.chat.id, f"string kamu\n{cek.text}")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)



__MODULE__ = "Misc"
__HELP__ = """
<b>✅ All User
<i>
❧ `.limit` - Check Limit telegram from @SpamBot.
❧ `.webshot <link>` - To Screenshot a given web page.
❧ `.open` - To view the contents of the file as text which is sent as a telegram message.
</i></b>
"""