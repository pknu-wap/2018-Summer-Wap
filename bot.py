import asyncio
import discord
import newcheck_cr

client = discord.Client()

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

def run_bot():
    client.run('NDQyNjY5MDMzMzg5ODE3ODU5.DdCOyw.P5R3brPUiHPfK3DdxRCDaEVziJo')
