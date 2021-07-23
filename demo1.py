import asyncio
from telethon import TelegramClient, events
from telethon.tl.custom.message import Message
from telethon.client.downloads import DownloadMethods
from telethon.utils import get_input_location
# from pyaxmlparser import APK
import cryptg
from FastTelethonhelper import download_without_progressbar

api_id, api_hash = 936087, '5f6f172f2107d79ed3e2929075a78058'
client = TelegramClient('telethon_session',api_id, api_hash)
client.start()

print('initated...')
@client.on(events.NewMessage(pattern="/start"))
async def demo(event):
    print('1')
    async for i in client.iter_messages('MyGoogleDrive0',limit=1):
        print('started')
        downloaded_location = await download_without_progressbar(client, i.media)
        print('donedoenloaded ',downloaded_location)


client.run_until_disconnected()
