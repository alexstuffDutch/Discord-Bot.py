import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix="?")

@client.event
async def on_message(message):
    if message.content.upper().startswith('P!REPORT'):
        userID = message.author.id
        server = client.get_server("363386694868664320")
        args = message.content.split(" ")
        await client.send_message(server.get_channel("444592474699071508"),  "%s" % (" ".join(args[1:])))
        await client.send_message(message.author, "Send **succ**essfully!")
        await client.send_message(server.get_channel("444924917763407892"), "<@%s> reported" % (userID))
                
    if message.content.upper().startswith('P!INVITE'):
        await client.send_message(message.author, "https://discord.gg/CQp5rdJ")
        userID = message.author.id
        server = client.get_server("363386694868664320")
        await client.send_message(server.get_channel("444924917763407892"), "<@%s> requested a invite link." % (userID))
        await client.send_message(message.channel, "<@%s> Check your DMs!" % (userID))

    if message.content.upper().startswith('P!SHUTDOWN'):
        if message.author.id == "346546938490912768":
            server = client.get_server("363386694868664320")
            await client.send_message(message.channel, "Announcing shutdown!")
            await client.send_message(server.get_channel("444857761587527681"), "Bot is going to shutdown!")
            await client.change_presence(game=discord.Game(name='Going to shutdown!'))
        else:
            await client.send_message(message.channel, "You do not have permission!")

    if message.content.upper().startswith('P!HELP'):
        embed=discord.Embed(title="Bot help", description="Help list", color=0x00ff00)
        embed.add_field(name="Commands", value="Just say p!cmds for commands", inline=False)
        embed.add_field(name="About", value="This bot is a bot for Pizza People, the goal of this bot is to make Pizza People safer, cleaner and more efficient. Its goal is also to bring up fun and happyness.", inline=False)
        await client.send_message(message.channel, embed=embed)
        
    if message.content.upper().startswith('P!QOTD'):
        if "444592342293282820" in [role.id for role in message.author.roles]:
            userID = message.author.id
            server = client.get_server("363386694868664320")
            args = message.content.split(" ")
            await client.send_message(server.get_channel("459021735807811594"),  "%s" % (" ".join(args[1:])))   
            await client.send_message(server.get_channel("444924917763407892"), "<@%s> set the QOTD" % (userID))
        else:
            await client.send_message(message.channel, "You are not allowed")


    if message.content.upper().startswith('P!CMDS'):
        embed=discord.Embed(title="Commands", description="Commands list", color=0x00ff00)
        embed.add_field(name="P!REPORT", value="This will let admins know with the message you have given, but you are most likely to be questioned, and also, abusing this will get you to a warning. Use this like this: P!REPORT [MESSAGE].", inline=False)
        embed.add_field(name="P!INVITE", value="This will let you show an invite for inviting people.", inline=False)
        embed.add_field(name="Admin Commands", value="Under is for admins, regular people cannot access these commands.", inline=False)
        embed.add_field(name="P!QOTD", value="Lets the bot say the QOTD in the #qotd channel. Use it like this: P!QOTD [QOTD].", inline=False)
        embed.add_field(name="----", value="Currently in progress, please do not steal the script, thank you.")
        await client.send_message(message.channel, embed=embed)
            
            
        
                      
        
        

                                             
@client.event
async def on_ready():
    server = client.get_server("363386694868664320")
    await client.send_message(server.get_channel("444857761587527681"), "Bot is ready and up! Current version is 0.2.8")
    await client.change_presence(game=discord.Game(name="Making pizzas!"))
    

        
client.run("NDQ0MTYxNjQ3MDI4ODYyOTc2.DdjJgg.lsgqAMpYLLIqJunIR4t70Xx-fa8")
