from pyrogram import Client, idle, filters
from pyrogram.types import Message


@Client.on_message(filters.private & filters.command("start"))
async def start_bot(_, ctx: Message):
    form = await _.send_message(ctx.chat.id, f"hello")
    
@Client.on_message(filters.private & filters.command("form"))
async def form_bot(_, ctx: Message):
    try:
        awal = await _.send_message(ctx.chat.id, f"👮🏻‍♀️ **Memulai mengisi formulir!!**\n\nSilakan isi dengan benar,jika ada pertanyaan silakan hubungin [admin](https://t.me/phobiakalian)")
        Nama = ctx.from_user.first_name
        id = ctx.chat.id
        password = await ctx.chat.ask("Ketikan password anda!!")
        password2 = await ctx.chat.ask("konfimasi password!!")
        if password2.text != password.text:
            return await _.send_message(ctx.chat.id, f"password tidak sesuai")
        await _.send_message(ctx.chat.id, f"Selamat!!\n\nNama : {nama.text}\nID : {id.text}\nPassword : {password2.text}")
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
