# This example requires the 'message_content' intent.
import requests
import discord
from readtable import (
    lookupMove,
    lookupMoveList,
    findHitbox,
    findCharPic,
    getCharByAlias,
)
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

characterList = [
    "Anakaris",
    "Aulbath",
    "Bishamon",
    "Bulleta",
    "Demitri",
    "Felicia",
    "Gallon",
    "Jedah",
    "Lei-Lei",
    "Lilith",
    "Morrigan",
    "Q-Bee",
    "Sasquatch",
    "Victor",
    "Zabel",
]

charAliases = {
    "Anakaris": ["Anakaris", "anakaris", "anak", "AN", "an"],
    "Aulbath": ["Aulbath", "aulbath", "fish", "AU", "au"],
    "Bishamon": ["Bishamon", "bishamon", "bish", "BI", "bi"],
    "Bulleta": ["Bulleta", "bulleta", "bul", "bull", "BU", "bu"],
    "Demitri": ["Demitri", "demitri", "dem", "DE", "de"],
    "Felicia": ["Felicia", "felicia", "fel", "cat", "FE", "fe"],
    "Gallon": ["Gallon", "gallon", "gal", "wolf", "GA", "ga"],
    "Jedah": ["Jedah", "jedah", "jed", "JE", "je"],
    "Lei-Lei": ["Lei-Lei", "lei-lei", "lei", "leilei", "LE", "le", "Lei-lei"],
    "Lilith": ["Lilith", "lilith", "lil", "LI", "li"],
    "Morrigan": ["Morrigan", "morrigan", "mor", "MO", "mo"],
    "Q-Bee": ["Q-Bee", "q-bee", "bee", "QB", "qb"],
    "Sasquatch": ["Sasquatch", "sasquatch", "sas", "SA", "sa"],
    "Victor": ["Victor", "victor", "vic", "VI", "vi"],
    "Zabel": ["Zabel", "zabel", "zab", "ZA", "za", "zombie"],
}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("VSAVbot"):
        try:
            messagesplit = message.content.split()
            inputChara = getCharByAlias(charAliases, messagesplit[1])
            # inputChara = messagesplit[1].capitalize()
            # if inputChara == "Lei-lei":
            #     inputChara = "Lei-Lei"
            # if inputChara == "Q-bee":
            #     inputChara = "Q-Bee"
            inputMove = messagesplit[2].upper()
        except:
            await message.channel.send(
                "Please enter a character and a move ('VSAVbot Victor 5LP'). To request the movelist enter character and 'movelist' ('VSAVbot Victor movelist')"
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_green(), description=inputMove, title=inputChara
        )

        if inputChara not in characterList:
            await message.channel.send(
                "Character does not exist. Use 'movelist' to return a character's movelist (VSAVbot Victor movelist)."
            )

        if inputMove == "MOVELIST":
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymovelist = lookupMoveList(inputChara)
            embed.add_field(name="movelist", value=displaymovelist)
            await message.channel.send(embed=embed)

        else:
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymoves = lookupMove(inputChara, inputMove)
            embed.add_field(name="", value=str(displaymoves))
            displayHitboxes = findHitbox(inputChara, inputMove)
            try:
                for x in displayHitboxes:
                    # print(x)
                    embed.set_image(url=x)
                    # for some reason sending embed here will send all of the hitbox pics if there are multiple but in separate embeds
                    # await message.channel.send(embed=embed)
            except:
                await message.channel.send(
                    "Move does not exist. First letter of character name is capitalized. Use 'movelist' to return a character's movelist (VSAVbot Victor movelist)."
                )
            await message.channel.send(embed=embed)

    if message.content.startswith("vsavbot"):
        try:
            messagesplit = message.content.split()
            inputChara = getCharByAlias(charAliases, messagesplit[1])

            # inputChara = messagesplit[1].capitalize()
            # if inputChara == "Lei-lei":
            #     inputChara = "Lei-Lei"
            # if inputChara == "Q-bee":
            #     inputChara = "Q-Bee"
            inputMove = messagesplit[2].upper()
        except:
            await message.channel.send(
                "Please enter a character and a move ('VSAVbot Victor 5LP'). To request the movelist enter character and 'movelist' ('VSAVbot Victor movelist')"
            )

        embed = discord.Embed(
            colour=discord.Colour.dark_green(), description=inputMove, title=inputChara
        )

        if inputChara not in characterList:
            await message.channel.send(
                "Character does not exist. Use 'movelist' to return a character's movelist (VSAVbot Victor movelist)."
            )

        if inputMove == "MOVELIST":
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymovelist = lookupMoveList(inputChara)
            embed.add_field(name="movelist", value=displaymovelist)
            await message.channel.send(embed=embed)

        else:
            embed.set_thumbnail(url=findCharPic(inputChara))
            displaymoves = lookupMove(inputChara, inputMove)
            embed.add_field(name="", value=str(displaymoves))
            displayHitboxes = findHitbox(inputChara, inputMove)
            try:
                for x in displayHitboxes:
                    # print(x)
                    embed.set_image(url=x)
                    # for some reason sending embed here will send all of the hitbox pics if there are multiple but in separate embeds
                    # await message.channel.send(embed=embed)
            except:
                await message.channel.send(
                    "Move does not exist. First letter of character name is capitalized. Use 'movelist' to return a character's movelist (VSAVbot Victor movelist)."
                )
            await message.channel.send(embed=embed)

    if message.content.startswith("Ping page"):
        await message.channel.send(
            requests.get(
                "https://wiki.gbl.gg/index.php?title=Vampire_Savior/Aulbath/Data&action=edit"
            ).status_code
        )


DC_TOKEN = os.getenv("DC_TOKEN")
client.run(DC_TOKEN)
