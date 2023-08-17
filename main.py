import discord
import os, random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'наш ботик {bot.user} запущен!')

@bot.command
async def eco_practic(message):
    if message.content.startswith('$eco'):
        await message.channel.send("дома из конопли")


