import asyncio
import discord
import spyder
import json
from datetime import datetime

client = discord.Client()
channel = discord.Object(id='429660895858130966')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game = discord.Game(name = '코딩중 입니다...'))

@client.event
async def on_message(message):
    if message.content.startswith("!cr"):
        cr = newcheck_cr.get_for_test()
        await client.send_message(message.channel, cr)


async def send_notice():
    while 1:
        notice = spyder.get_newest_homepage()
        await client.wait_until_ready()
        await client.send_message(channel, f'현재시간 {datetime.now()} 기준 홈페이지 최신 공지사항\n' + json.dumps(notice[0], ensure_ascii = False, indent = 2))
        await client.send_message(channel, f'현재시간 {datetime.now()} 기준 데이터베이스 최신 공지사항\n' + spyder.get_newest_db())
        await asyncio.sleep(300)

def run_bot():
    client.loop.create_task(send_notice())
    client.run('NDQyNjY5MDMzMzg5ODE3ODU5.DdCOyw.P5R3brPUiHPfK3DdxRCDaEVziJo')

run_bot()
