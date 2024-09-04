# This example requires the 'message_content' intent.
import requests
import discord
from readtable import lookupMove, lookupMoveList, findHitbox, findCharPic
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('VSAVbot'):
        messagesplit = message.content.split()
        inputChara = messagesplit[1]
        inputMove = messagesplit[2]

        embed = discord.Embed(
            colour=discord.Colour.dark_green(),
            description=inputMove,
            title=inputChara
        )
        if inputMove == 'movelist':
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymovelist = lookupMoveList(inputChara)
            embed.add_field(name="movelist", value=displaymovelist)
            await message.channel.send(embed=embed)

        else:
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymoves = lookupMove(inputChara, inputMove)
            embed.add_field(name="", value=str(displaymoves))
            displayHitboxes = findHitbox(inputChara, inputMove)
            for x in displayHitboxes:
                #print(x)
                embed.set_image(url=x)
            await message.channel.send(embed=embed)

    if message.content.startswith('Ping page'):
        await message.channel.send(requests.get('https://wiki.gbl.gg/index.php?title=Vampire_Savior/Aulbath/Data&action=edit').status_code)
        
DC_TOKEN = os.getenv('DC_TOKEN')
client.run(DC_TOKEN)