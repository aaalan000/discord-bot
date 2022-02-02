#基礎
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= "/")

@bot.event

async def on_ready():
    print(">>Bot is online<<")

bot.run("OTM4NDExMDAyNTE1NTcwNzQ4.Yfp5WQ.TSQOXoirlZ6N2Jy-qA0TYIVInGE")

#成員加入離開提醒
@bot.event

async def on_member_join(member):
    channel = bot.get_channel(938444934967590973)
    await channel.send(f"{member}join!")

@bot.event

async def on_member_remove(member):
    channel = bot.get.channel(938444980081545246)
    await channel.send(f"{member}leave!")