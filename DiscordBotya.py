import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!SALES'):
        userID = message.author.id
        server = client.get_server("490938256683302912")
        args = message.content.split(" ")
        await client.send_message(server.get_channel("490942629916311562"), "%s" % (" ".join(args[1:])))
        await client.send_message(message.author, "A salesman will contact you! Thank you for buying!")
        await client.send_message(server.get_channel("490942613269250048"), "<@%s> requested a sale!" % (userID))
                   
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Handling sales!"))
    

        
client.run("NDkwOTQyNTAxOTQ4MjI3NTk3.DoGIZg.i41XMGvCYIxbM3tlrFFJG7qFg5A")
