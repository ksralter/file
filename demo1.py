import asyncio
from telethon import TelegramClient, events
from telethon.tl.custom.message import Message
from telethon.client.downloads import DownloadMethods
from telethon.utils import get_input_location
from pyaxmlparser import APK
import cryptg
from FastTelethonhelper import download_without_progressbar

api_id, api_hash = 936087, '5f6f172f2107d79ed3e2929075a78058'
client = TelegramClient('telethon_session',api_id, api_hash)
client.start()

@client.on(events.NewMessage(pattern="/start"))
async def demo(event):
    # m = await client.iter_messages('MyGoogleDrive0')
    print('1')
    # f = open('file.apk', 'wb')
    async for i in client.iter_messages('MyGoogleDrive2',limit=1):
        print('started')
        # print(i.document)

        downloaded_location = await download_without_progressbar(client, i)
        
        print('donedoenloaded ',downloaded_location)
        # x = await client.download_media(i)
        # print(x)
        # f.write(x)
        # f.close()
        # apk = APK(downloaded_location)
        # print(apk.package)

        # print(i.file.size)
        # x = await client.download_file(i)
        # print(x.file)
        # break


client.run_until_disconnected()