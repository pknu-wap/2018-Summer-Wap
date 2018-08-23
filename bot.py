import asyncio
import discord
import crawldata
import json
from datetime import datetime

client = discord.Client()
channel = discord.Object(id='481813369305956358')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = 'League of Legends'))



async def send_notice():
    while 1:
        before = crawldata.ce_before_update()
        crawldata.ce_update_data()
        after = crawldata.ce_after_update()

        await client.wait_until_ready()
        await client.send_message(channel, f'현재시간 {datetime.now()}\n'+ '컴퓨터공학과 공지사항 업데이트다링~\n' + crawldata.compare(before,after))
        await asyncio.sleep(7)


        before = crawldata.ocean_before_update()
        crawldata.ocean_update_data()
        after = crawldata.ocean_after_update()

        await client.wait_until_ready()
        await client.send_message(channel, f'현재시간 {datetime.now()}\n'+ 'IT공학과 공지사항 업데이트다링~\n' + crawldata.compare(before,after))
        await asyncio.sleep(7)


        before = crawldata.it_before_update()
        crawldata.it_update_data()
        after = crawldata.it_after_update()

        await client.wait_until_ready()
        await client.send_message(channel, f'현재시간 {datetime.now()}\n'+ '해양학과 공지사항 업데이트다링~\n' + crawldata.compare(before,after))
        await asyncio.sleep(10)



def run_bot():
    client.loop.create_task(send_notice())
    client.run('NDgxODA3ODg2OTc3MDczMTU0.Dl_sKA.RzPJkIVwLZAzZzuWpvLJTbRdZ9c')

run_bot()
