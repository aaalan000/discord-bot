#基礎
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= "/")

@bot.event

async def on_ready():
    print(">>Bot is online<<")

bot.run("")

#成員加入離開提醒
@bot.event

async def on_member_join(member):
    channel = bot.get_channel()
    await channel.send(f"{member}join!")

@bot.event

async def on_member_remove(member):
    channel = bot.get.channel()
    await channel.send(f"{member}leave!")