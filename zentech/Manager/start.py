from pyrogram import Client, idle, filters
from pyrogram.types import Message
from zentech.Database import get_authuser_names, save_authuser, delete_authuser, extract_user

async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


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
        await _.send_message(ctx.chat.id, f"Selamat!!\n\nNama : {Nama.text}\nID : {id.text}\nPassword : {password2.text}")
    except Exception as ex:
        print('Mistakes for connection')
        print(ex)

@Client.on_message(filters.command("auth") & filters.group)
async def auth(_, ctx: Message):
    chat_id = ctx.chat.id
    userid = await extract_user(ctx)
    await ctx.reply_text("auth CMD")
    if not ctx.reply_to_message:
        if len(ctx.command) != 2:
            return await ctx.reply_text("😕 Maaf, **Saya tidak bisa** menemukan pengguna ini!\n\n» coba beri saya id atau username pengguna tersebut")
        user = ctx.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await _.get_users(user)
        user_id = ctx.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = ctx.from_user.first_name
        from_user_id = ctx.from_user.id
        _check = await get_authuser_names(ctx.chat.id)
        count = 0 
        for smex in _check:
            count += 1
        if int(count) == 20:
            return await ctx.reply_text("😕 Anda hanya dapat memiliki 20 Pengguna dalam daftar pengguna **resmi** grup Anda.")
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            await save_authuser(ctx.chat.id, token, assis)
            mention = user.mention
            await ctx.reply_text(f"🧙 **menambahkan** {mention} ke **daftar pengguna resmi**, mulai sekarang dia bisa **menggunakan** perintah **Admin.**")
            return
        else:
            return await ctx.reply_text(f"{mention} sudah ada di **daftar pengguna resmi** dan dia dapat menggunakan **perintah admin.**")
    from_user_id = ctx.from_user.id
    user_id = ctx.reply_to_message.from_user.id
    user_name = ctx.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = ctx.from_user.first_name
    _check = await get_authuser_names(ctx.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 20:
        return await ctx.reply_text("😕 Anda hanya dapat memiliki 20 Pengguna dalam daftar pengguna **resmi** grup Anda.")
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        await save_authuser(ctx.chat.id, token, assis)
        await ctx.reply_text(f"🧙 **menambahkan** {ctx.reply_to_message.from_user.mention} ke **daftar pengguna resmi**, mulai sekarang dia bisa **menggunakan** perintah **Admin.**")
        return
    else:
        return await ctx.reply_text(
            f"{ctx.reply_to_message.from_user.mention} sudah ada di **daftar pengguna resmi** dan dia dapat menggunakan **perintah admin.**")

__MODULE__ = "Misc"
__HELP__ = """
<b>✅ All User
<i>
❧ `.limit` - Check Limit telegram from @SpamBot.
❧ `.webshot <link>` - To Screenshot a given web page.
❧ `.open` - To view the contents of the file as text which is sent as a telegram message.
</i></b>
"""
