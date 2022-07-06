from dotenv import load_dotenv
import discord
import os
from main import getBestChamps

# Variables for Bot
load_dotenv();
TOKEN = os.getenv('token')
client = discord.Client()

# Commands
commands = [
        {"cmd": "!fabrzylol", "tag": "Fabrzy"},
        {"cmd": "!renzolol", "tag": "Renzo98"},
        {"cmd": "!deonlol", "tag": "thatboidobi"},
        {"cmd": "!jodaddylol", "tag": "Jodaddy1231"},
        {"cmd": "!codylol", "tag": "Draxal"},
        {"cmd": "!demetrilol", "tag": "Demetri33"}
        ]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    user_message = str(message.content)
    response = "Best Champs: "
    for x in commands:
        if user_message == x["cmd"]:
            list_of_champs = getBestChamps(x["tag"])
            for y in list_of_champs:
                response += y
                response += " "

            await message.channel.send(response)

client.run(TOKEN)

