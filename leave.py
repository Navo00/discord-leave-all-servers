import discord
from discord.ext import commands, tasks





client = discord.Client()   
client= commands.Bot(command_prefix="none", self_bot=True)
client.remove_command("help")
token = "eyJpZCI6MTAxNTczOTI1NTEwNjA0ODE1MCwiZW1haWwiOiJmdWtkYWRpc2NvcmRAb3V0bG9vay5jb20ifQ.YxPL7Q.HnVdvzZbqPer9ROj05BhUvySwWQ"






@client.event
async def on_connect():
    for guild in client.guilds:
        try: 
             await guild.leave()
        except:
            print("Cannot leave server")

client.run(token, reconnect=True, bot=False)
