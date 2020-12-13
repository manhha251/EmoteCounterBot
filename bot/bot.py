# bot.py
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from configparser import ConfigParser

# Load environment
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Init bot
bot = commands.Bot(command_prefix="!")

# Load data
data = ConfigParser()
data.read("data.ini")

if not data.has_section("EMOJI"):
    data["EMOJI"] = {}
emoji_list = data["EMOJI"]
print(emoji for emoji in emoji_list)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='hello')
async def on_message(ctx):
    await ctx.send('Hello World!')


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


if __name__ == "__main__":
    bot.run(TOKEN)
