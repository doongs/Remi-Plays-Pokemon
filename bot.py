import discord
import time
import demoji
import glob
import os
from random import randint
import keyboard
from imgurpython import ImgurClient

client = discord.Client()

imgur = ImgurClient('0f2f40f4ecbaefe',
                    '1ef45c9734769d07cd887c012268ced98caa0de5')

nextUpdate = "N/A"
lastInput = "Up"
inputDict = {'upwards button': 'up', 'downwards button': 'down', 'reverse button': 'left',
             'play button': 'right', 'A button (blood type)': 'a', 'B button (blood type)': 'b', 'stop button': 'c', 'record button': 'd'}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # main game loop
    lastInput = await calculate_input()
    send_input(lastInput)
    time.sleep(10)
    screenshot()
    await send_update(read_file())
    # time.sleep(1800)

# add reactions to the recently sent embed


@client.event
async def on_message(message):
    if message.author == client.user:
        await message.add_reaction('🔼')
        await message.add_reaction('🔽')
        await message.add_reaction('◀️')
        await message.add_reaction('▶️')
        await message.add_reaction('🅰️')
        await message.add_reaction('🅱️')
        await message.add_reaction('⏹️')
        await message.add_reaction('⏺️')
        return

# send the embed message to the chat containing the screenshot


async def send_update(num):
    channel = client.get_channel(798266793134653480)
    embed = discord.Embed(
        title=num, color=0xad1457)
    embed.set_footer(text=f'Next Update: {nextUpdate}')
    # embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/798205629130473514/4c04457c9ea70ff98af3c9470d22cb50.png?size=64')
    embed.set_image(url=imgur.upload_from_path(
        'snips\Pokemon - Emerald Version (U)-0.png', config=None, anon=True)['link'])
    await channel.send(embed=embed)


def send_input(input):
    print(input)
    time.sleep(2)
    print('press')
    keyboard.press(input)
    time.sleep(2)
    print('release')
    keyboard.release(input)
    time.sleep(2)


async def calculate_input():
    channel = client.get_channel(798266793134653480)
    lastMessage = await channel.fetch_message(channel.last_message_id)
    votedInput = ""
    max = 0
    for input in lastMessage.reactions:
        # print(demoji.replace_with_desc(input.emoji,""))
        if input.count > max:
            votedInput = demoji.replace_with_desc(input.emoji, "")
            max = input.count
        elif input.count == max:
            if randint(0, 1) == 0:
                votedInput = demoji.replace_with_desc(input.emoji, "")
    return inputDict.get(votedInput)


def screenshot():
    mypath = "snips"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    send_input('l')
    return

def read_file():
    file = open('input.txt', 'r') 
    num = 0
    num = int(file.read()) + 1 
    file.close()
    open('file.txt', 'w').close()
    file = open('input.txt', 'w')
    file.write(str(num))
    file.close
    return num
    

client.run('Nzk4MjA1NjI5MTMwNDczNTE0.X_xo6w.XJ2e1ATKaORgfpvHMw5xdSmZGZs')
