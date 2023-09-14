import asyncio
import time
from datetime import datetime
from Abg import patch
from aiohttp import ClientSession
from pyrogram import Client
from pyrogram import Client
MOD_LOAD = []
MOD_NOLOAD = []


StartTime = time.time()

START_TIME = datetime.now()

loop = asyncio.get_event_loop()
aiohttpsession = ClientSession()

API_ID = 3563677
API_HASH = "483c51115c56b7d44111bd0fe31cc9cf"
BOT_TOKEN = "6488957061:AAEmI6bps5NV7rWGaw5FBBW2UiDdDlABS_o"

app = Client(
    name="app2", 
    bot_token=BOT_TOKEN, 
    api_id=API_ID, 
    api_hash=API_HASH,
    plugins={"root": "zentech.Manager"},
)
app.start()
