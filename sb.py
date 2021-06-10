import discord
from discord.ext import commands

token = "Discord Token"
prefix = "."
SB = discord.Client()
SB = commands.Bot(command_prefix=prefix, self_bot=True)
SB.remove_command('help')




@SB.event
async def on_ready():
    print("started")

@SB.command()
async def test(ctx):
    await ctx.send("Test Message!")


SB.run(token, bot=False)
